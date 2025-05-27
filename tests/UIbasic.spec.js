const { test } = require('@playwright/test')


test('browser test case', async ({ browser }) => {

    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto('https://uat.elyxr.ai/login')
    
}
);

test('page test case', async ({ page }) => {

    await page.goto('https://uat.elyxr.ai/login')
    
}
);