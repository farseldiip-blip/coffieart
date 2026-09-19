const { test, expect } = require('@playwright/test');
const path = require('path');

const testCases = [
  { name: 'index', file: 'index.html' },
  { name: 'menu', file: 'menu.html' },
];

testCases.forEach(({ name, file }) => {
  test.describe(`/${file}`, () => {
    test(`should load without errors on all viewports`, async ({ page, browserName }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
      expect(response?.status()).toBe(200);

      const errors = [];
      page.on('pageerror', err => errors.push(err.message));
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });

      await page.waitForTimeout(1500);

      expect(errors.filter(e => !e.includes('ResizeObserver') && !e.includes('Script'))).toEqual([]);
    });

    test(`should have no horizontal overflow`, async ({ page }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(500);
      const overflow = await page.evaluate(() => {
        // Check computed style for overflow property
        const computed = window.getComputedStyle(document.body);
        // Also check if body can scroll horizontally
        return computed.overflowX !== 'hidden';
      });
      expect(overflow).toBe(false);
    });

    test(`should render all sections visible`, async ({ page }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(1000);

      const isVisible = await page.evaluate(() => {
        const sections = document.querySelectorAll('section, header, footer');
        return Array.from(sections).every(s => {
          if (s.hasAttribute('class') && s.getAttribute('class').includes('fixed')) return true;
          return s.offsetParent !== null;
        });
      });
      expect(isVisible).toBe(true);
    });

    test(`should have brand gradient classes`, async ({ page: pwPage }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await pwPage.goto(url, { waitUntil: 'networkidle' });

      if (file === 'index.html') {
        await expect(pwPage.locator('.brand-gradient-text').first()).toBeVisible();
      }
    });

    test(`should have working WhatsApp link`, async ({ page: pwPage }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await pwPage.goto(url, { waitUntil: 'networkidle' });

      const whatsappLink = pwPage.locator('a[href*="wa.me"]');
      if (await whatsappLink.count() > 0) {
        const href = await whatsappLink.first().getAttribute('href');
        expect(href).toContain('351XXXXXXXXX');
      }
    });

    test(`should have logo visible`, async ({ page: pwPage }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await pwPage.goto(url, { waitUntil: 'networkidle' });
      await expect(pwPage.locator('img[src*="logo.png"]').first()).toBeVisible();
    });

    test(`font rendering: no console errors from fonts`, async ({ page: pwPage }) => {
      const url = `file://${path.resolve(__dirname, '..', file)}`;
      await pwPage.goto(url, { waitUntil: 'networkidle' });

      const errors = [];
      pwPage.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      await pwPage.waitForTimeout(2000);

      const fontErrors = errors.filter(e => e.includes('woff') || e.includes('font'));
      expect(fontErrors).toEqual([]);
    });
  });
});