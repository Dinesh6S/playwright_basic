const { test, expect } = require('@playwright/test')


test('browser test case', async ({ browser }) => {

    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto('https://uat.elyxr.ai/login')

    console.log(await page.title());
    
}
);

test('page test case', async ({ page }) => {

    await page.goto('https://google.com');

    console.log(await page.title());

    await expect(page).toHaveTitle('Google')
    
}
);