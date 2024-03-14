const {chromium} = require('playwright');

(async() => {
    const browser = await chromium.launch({headless:false, slowMo: 800})
    const context = await browser.newContext()
    const page = await browser.newPage()
    await page.goto('https://react-redux.realworld.io/#/login')

    await page.fill('input[type = "email"]', 'nobrulg21@gmail.com')
    await page.fill('input[type = "password"]', '12345')
    await page.click('form >> "Sign in"', {position: {x: 0, y: 0}, button: 'left', modifiers: ['Shift'], force: true, timeout: 45000})
    await page.focus('form >> "Sign in"')

    await browser.close()
}) ()