const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  use: {
    browserName: 'chromium',
  },
  projects: [
    { name: '360px', use: { viewport: { width: 360, height: 640 }, isMobile: true, hasTouch: true } },
    { name: '390px', use: { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } },
    { name: '430px', use: { viewport: { width: 430, height: 932 }, isMobile: true, hasTouch: true } },
    { name: '768px', use: { viewport: { width: 768, height: 1024 } } },
    { name: '1024px', use: { viewport: { width: 1024, height: 768 } } },
    { name: '1440px', use: { viewport: { width: 1440, height: 900 } } },
  ],
});