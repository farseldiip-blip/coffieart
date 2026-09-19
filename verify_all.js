const { chromium } = require('@playwright/test');
const path = require('path');
const fs = require('fs');

(async () => {
    const browser = await chromium.launch();
    
    const pages = [
        { file: 'index.html', title: 'Landing Page' },
        { file: 'menu.html', title: 'Menu Page' }
    ];

    const viewports = [
        { name: 'mobile-320', width: 320, height: 640 },
        { name: 'mobile-390', width: 390, height: 844 },
        { name: 'desktop-1440', width: 1440, height: 900 }
    ];

    for (const p of pages) {
        console.log(`\n========================================`);
        console.log(`Testing ${p.title} (${p.file})`);
        console.log(`========================================`);

        for (const vp of viewports) {
            const context = await browser.newContext({
                viewport: { width: vp.width, height: vp.height },
                deviceScaleFactor: 2
            });
            const page = await context.newPage();
            
            const errors = [];
            page.on('pageerror', err => errors.push(err.message));
            page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });

            const url = 'file://' + path.resolve(p.file);
            await page.goto(url, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(600);

            // 1. Horizontal overflow check
            const overflow = await page.evaluate(() => {
                return document.documentElement.scrollWidth > window.innerWidth || document.body.scrollWidth > window.innerWidth;
            });

            // 2. Sections visible check
            const sectionsVisible = await page.evaluate(() => {
                const sections = document.querySelectorAll('section, header, footer');
                return Array.from(sections).every(s => s.offsetParent !== null || window.getComputedStyle(s).position === 'fixed');
            });

            // 3. Logo visible
            const logoVisible = await page.evaluate(() => {
                const logo = document.querySelector('img[src*="logo.png"]');
                return logo && logo.offsetWidth > 0 && logo.offsetHeight > 0;
            });

            // 4. WhatsApp link
            const whatsappValid = await page.evaluate(() => {
                const wa = document.querySelector('a[href*="wa.me"]');
                return wa && wa.getAttribute('href').includes('351XXXXXXXXX');
            });

            // 5. Mobile bottom bar display
            const bottomBarState = await page.evaluate(() => {
                const bar = document.querySelector('.mobile-bottom-bar');
                if (!bar) return 'not found';
                return window.getComputedStyle(bar).display;
            });

            console.log(`[${p.file} @ ${vp.name}]`);
            console.log(`  - Console errors: ${errors.length === 0 ? 'PASS (0)' : 'FAIL: ' + JSON.stringify(errors)}`);
            console.log(`  - Horizontal overflow: ${!overflow ? 'PASS (None)' : 'FAIL (Overflow detected)'}`);
            console.log(`  - Sections visible: ${sectionsVisible ? 'PASS' : 'FAIL'}`);
            console.log(`  - Logo visible: ${logoVisible ? 'PASS' : 'FAIL'}`);
            console.log(`  - WhatsApp link: ${whatsappValid ? 'PASS' : 'FAIL'}`);
            console.log(`  - Bottom bar display: ${bottomBarState} (${vp.width < 768 ? 'expected flex' : 'expected none'})`);

            // Screenshot for visual record
            const ssName = `shot_${p.file.replace('.html','')}_${vp.name}.png`;
            await page.screenshot({ path: ssName, fullPage: false });
            console.log(`  - Saved screenshot: ${ssName}`);

            // Test Lightbox on index.html
            if (p.file === 'index.html' && vp.name === 'desktop-1440') {
                const card = await page.locator('.gallery-card').first();
                await card.click();
                await page.waitForTimeout(300);
                const isLightboxActive = await page.evaluate(() => {
                    const modal = document.getElementById('lightboxModal');
                    return modal && modal.classList.contains('active');
                });
                console.log(`  - Lightbox open test: ${isLightboxActive ? 'PASS' : 'FAIL'}`);
                
                // Press Escape to close
                await page.keyboard.press('Escape');
                await page.waitForTimeout(300);
                const isLightboxClosed = await page.evaluate(() => {
                    const modal = document.getElementById('lightboxModal');
                    return modal && !modal.classList.contains('active');
                });
                console.log(`  - Lightbox close on Escape: ${isLightboxClosed ? 'PASS' : 'FAIL'}`);
            }

            await context.close();
        }
    }

    await browser.close();
    console.log('\nAll tests and validations finished!');
})();
