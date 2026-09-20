# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests\qa.spec.js >> /menu.html >> should have working WhatsApp link
- Location: tests\qa.spec.js:62:5

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: page.goto: Test timeout of 30000ms exceeded.
Call log:
  - navigating to "file:///D:/code/coffieart/menu.html", waiting until "networkidle"

```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - banner [ref=e2]:
    - generic [ref=e3]:
      - link "KOFFIE ART Home" [ref=e4] [cursor=pointer]:
        - /url: index.html
        - img "KOFFIE ART logo" [ref=e6]
        - generic [ref=e7]: KOFFIE ART
      - button "Open navigation menu" [ref=e8] [cursor=pointer]:
        - generic [ref=e9]: menu
  - main [ref=e10]:
    - link "Back to Home" [ref=e13] [cursor=pointer]:
      - /url: index.html
      - generic [ref=e14]: arrow_back
    - region "KOFFIE ART Menu Pages" [ref=e16]:
      - generic [ref=e17]:
        - button "View KOFFIE ART menu, page 1 of 7 full screen" [ref=e18]:
          - img "KOFFIE ART menu, page 1 of 7" [ref=e19]
        - button "View KOFFIE ART menu, page 2 of 7 full screen" [ref=e20]:
          - img "KOFFIE ART menu, page 2 of 7" [ref=e21]
        - button "View KOFFIE ART menu, page 3 of 7 full screen" [ref=e22]:
          - img "KOFFIE ART menu, page 3 of 7" [ref=e23]
        - button "View KOFFIE ART menu, page 4 of 7 full screen" [ref=e24]:
          - img "KOFFIE ART menu, page 4 of 7" [ref=e25]
        - button "View KOFFIE ART menu, page 5 of 7 full screen" [ref=e26]:
          - img "KOFFIE ART menu, page 5 of 7" [ref=e27]
        - button "View KOFFIE ART menu, page 6 of 7 full screen" [ref=e28]:
          - img "KOFFIE ART menu, page 6 of 7" [ref=e29]
        - button "View KOFFIE ART menu, page 7 of 7 full screen" [ref=e30]:
          - img "KOFFIE ART menu, page 7 of 7" [ref=e31]
  - contentinfo [ref=e32]:
    - generic [ref=e33]:
      - generic [ref=e34]:
        - generic [ref=e35]:
          - generic [ref=e36]:
            - img "KOFFIE ART logo" [ref=e38]
            - generic [ref=e39]: KOFFIE ART
          - paragraph [ref=e40]: House-roasted specialty coffee and desserts, crafted with care in the heart of Mansoura.
          - generic [ref=e41]:
            - link "KOFFIE ART on Instagram" [ref=e42] [cursor=pointer]:
              - /url: https://instagram.com/koffieart
              - generic [ref=e43]: photo_camera
            - link "KOFFIE ART on WhatsApp" [ref=e44] [cursor=pointer]:
              - /url: https://wa.me/351XXXXXXXXX
              - generic [ref=e45]: chat
        - generic [ref=e46]:
          - heading "Quick Links" [level=3] [ref=e47]
          - list [ref=e48]:
            - listitem [ref=e49]:
              - link "Home" [ref=e50] [cursor=pointer]:
                - /url: index.html
            - listitem [ref=e51]:
              - link "Gallery" [ref=e52] [cursor=pointer]:
                - /url: index.html#gallery
            - listitem [ref=e53]:
              - link "Hours & Location" [ref=e54] [cursor=pointer]:
                - /url: index.html#visit
            - listitem [ref=e55]:
              - link "Contact" [ref=e56] [cursor=pointer]:
                - /url: index.html#contact
        - generic [ref=e57]:
          - heading "Visit Us" [level=3] [ref=e58]
          - paragraph [ref=e59]: El-Geish St., Mansoura, Egypt
          - paragraph [ref=e60]: "Sat – Thu: 10 AM – 12 AM"
          - paragraph [ref=e61]: "Friday: 1 PM – 12 AM"
      - generic [ref=e62]:
        - paragraph [ref=e63]: © 2024 KOFFIE ART. All rights reserved. Specialty Coffee · Mansoura, Egypt.
        - paragraph [ref=e64]: Designed with care for coffee lovers.
```

# Test source

```ts
  1  | const { test, expect } = require('@playwright/test');
  2  | const path = require('path');
  3  | 
  4  | const testCases = [
  5  |   { name: 'index', file: 'index.html' },
  6  |   { name: 'menu', file: 'menu.html' },
  7  | ];
  8  | 
  9  | testCases.forEach(({ name, file }) => {
  10 |   test.describe(`/${file}`, () => {
  11 |     test(`should load without errors on all viewports`, async ({ page, browserName }) => {
  12 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  13 |       const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  14 |       expect(response?.status()).toBe(200);
  15 | 
  16 |       const errors = [];
  17 |       page.on('pageerror', err => errors.push(err.message));
  18 |       page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  19 | 
  20 |       await page.waitForTimeout(1500);
  21 | 
  22 |       expect(errors.filter(e => !e.includes('ResizeObserver') && !e.includes('Script'))).toEqual([]);
  23 |     });
  24 | 
  25 |     test(`should have no horizontal overflow`, async ({ page }) => {
  26 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  27 |       await page.goto(url, { waitUntil: 'networkidle' });
  28 |       await page.waitForTimeout(500);
  29 |       const overflow = await page.evaluate(() => {
  30 |         // Check computed style for overflow property
  31 |         const computed = window.getComputedStyle(document.body);
  32 |         // Also check if body can scroll horizontally
  33 |         return computed.overflowX !== 'hidden';
  34 |       });
  35 |       expect(overflow).toBe(false);
  36 |     });
  37 | 
  38 |     test(`should render all sections visible`, async ({ page }) => {
  39 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  40 |       await page.goto(url, { waitUntil: 'networkidle' });
  41 |       await page.waitForTimeout(1000);
  42 | 
  43 |       const isVisible = await page.evaluate(() => {
  44 |         const sections = document.querySelectorAll('section, header, footer');
  45 |         return Array.from(sections).every(s => {
  46 |           if (s.hasAttribute('class') && s.getAttribute('class').includes('fixed')) return true;
  47 |           return s.offsetParent !== null;
  48 |         });
  49 |       });
  50 |       expect(isVisible).toBe(true);
  51 |     });
  52 | 
  53 |     test(`should have brand gradient classes`, async ({ page: pwPage }) => {
  54 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  55 |       await pwPage.goto(url, { waitUntil: 'networkidle' });
  56 | 
  57 |       if (file === 'index.html') {
  58 |         await expect(pwPage.locator('.brand-gradient-text').first()).toBeVisible();
  59 |       }
  60 |     });
  61 | 
  62 |     test(`should have working WhatsApp link`, async ({ page: pwPage }) => {
  63 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
> 64 |       await pwPage.goto(url, { waitUntil: 'networkidle' });
     |                    ^ Error: page.goto: Test timeout of 30000ms exceeded.
  65 | 
  66 |       const whatsappLink = pwPage.locator('a[href*="wa.me"]');
  67 |       if (await whatsappLink.count() > 0) {
  68 |         const href = await whatsappLink.first().getAttribute('href');
  69 |         expect(href).toContain('351XXXXXXXXX');
  70 |       }
  71 |     });
  72 | 
  73 |     test(`should have logo visible`, async ({ page: pwPage }) => {
  74 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  75 |       await pwPage.goto(url, { waitUntil: 'networkidle' });
  76 |       await expect(pwPage.locator('img[src*="logo.png"]').first()).toBeVisible();
  77 |     });
  78 | 
  79 |     test(`font rendering: no console errors from fonts`, async ({ page: pwPage }) => {
  80 |       const url = `file://${path.resolve(__dirname, '..', file)}`;
  81 |       await pwPage.goto(url, { waitUntil: 'networkidle' });
  82 | 
  83 |       const errors = [];
  84 |       pwPage.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  85 |       await pwPage.waitForTimeout(2000);
  86 | 
  87 |       const fontErrors = errors.filter(e => e.includes('woff') || e.includes('font'));
  88 |       expect(fontErrors).toEqual([]);
  89 |     });
  90 |   });
  91 | });
```