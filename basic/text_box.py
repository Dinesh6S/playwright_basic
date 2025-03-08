from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launches a new Chromium browser instance
    browser = p.chromium.launch(headless=False)
    # Creates a new browser context
    context = browser.new_context()
    # to capture the logs and actions performed while running the script
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # to open a new tab/page
    page = context.new_page()
    # to open a website
    page.goto("https://demoqa.com/")
    # to get the attribute value
    print(page.locator('.banner-image').get_attribute('alt'))

    elements = page.get_by_text("Elements")
    elements.click()

    page.get_by_text("Please select an item from left to start practice.")

    time.sleep(3)
    options = page.locator('//div[@class="element-list collapse show"]//li')
    
    print(options.count())

    for option in options.all():
        # to get the text from the element
        print(option.text_content())

    options.nth(0).click()

    page.get_by_placeholder("Full Name").fill('user_name')
    page.get_by_placeholder("name@example.com").fill('myemail@yopmail.com')
    page.get_by_placeholder("Current Address").fill('my address')
    page.locator("//textarea[@id='permanentAddress']").fill('my permanent address')


    page.get_by_role("button", name='Submit').click()

    output_options = page.locator('//div[@id="output"]//p')

    for option in output_options.all():
        print(option.text_content())
    
    # to take a screen shot with fill page
    page.screenshot(path="screenshot.png", full_page=True)

    print("Page Title:", page.title())
    # to stop the trace and to create a new file for that
    context.tracing.stop(path = "trace.zip")
    # to close the page
    page.close()
    # to close the browser
    browser.close()
