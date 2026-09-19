const { chromium } = require('@playwright/test');
const path = require('path');
const fs = require('fs');

(async () => {
    const browser = await chromium.launch();
    
    // Viewports to test
    const viewports = [
        { name: 'mobile-320', width: 320, height: 600 },
        { name: 'mobile-390', width: 390, height: 844 },
        { name: 'desktop-1440', width: 1440, height: 900 }
    ];

    for (const vp of viewports) {
        const context = await browser.newContext({
            viewport: { width: vp.width, height: vp.height },
            deviceScaleFactor: 2
        });
        const page = await context.newPage();
        
        const errors = [];
        page.on('pageerror', err => errors.push(err.message));
        page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });

        const url = 'file://' + path.resolve('index.html');
        await page.goto(url, { waitUntil: 'domcontentloaded' });
        await page.waitForTimeout(1000);

        // Check horizontal overflow
        const overflow = await page.evaluate(() => {
            return document.documentElement.scrollWidth > window.innerWidth || document.body.scrollWidth > window.innerWidth;
        });

        // Check hero elements
        const heroInfo = await page.evaluate(() => {
            const hero = document.querySelector('.hero');
            const h1 = document.querySelector('.hero__title');
            const eyebrow = document.querySelector('.hero__eyebrow');
            const pill = document.querySelector('#heroOpenStatus');
            const primaryCta = document.querySelector('#heroCtaMenu');
            const dirCta = document.querySelector('#heroCtaDirections');
            const waCta = document.querySelector('#heroCtaWhatsapp');
            const bottomBar = document.querySelector('.mobile-bottom-bar');
            
            return {
                heroMinHeight: window.getComputedStyle(hero).minHeight,
                heroHeight: hero.offsetHeight,
                h1Text: h1 ? h1.textContent.trim() : null,
                eyebrowText: eyebrow ? eyebrow.textContent.trim() : null,
                pillText: pill ? pill.textContent.trim() : null,
                primaryHref: primaryCta ? primaryCta.getAttribute('href') : null,
                dirHref: dirCta ? dirCta.getAttribute('href') : null,
                waHref: waCta ? waCta.getAttribute('href') : null,
                bottomBarDisplay: bottomBar ? window.getComputedStyle(bottomBar).display : null
            };
        });

        console.log('=== Viewport ' + vp.name + ' ===');
        console.log('Errors:', errors);
        console.log('Horizontal overflow:', overflow);
        console.log('Hero info:', JSON.stringify(heroInfo, null, 2));

        // Take hero screenshot
        await page.screenshot({ path: 'test_' + vp.name + '.png', clip: { x: 0, y: 0, width: vp.width, height: Math.min(vp.height, 900) } });
        console.log('Saved test_' + vp.name + '.png');
        await context.close();
    }

    await browser.close();
    console.log('All automated checks completed successfully!');
})();
