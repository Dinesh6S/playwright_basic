from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://demoqa.com/")
    # to get the attribute value
    print(page.locator('.banner-image').get_attribute('alt'))

    elements = page.get_by_text("Alerts, Frame & Windows")
    elements.click()

    page.get_by_text("Please select an item from left to start practice.")

    time.sleep(3)
    options = page.locator('//div[@class="element-list collapse show"]//li')
    
    print(options.count())

    for option in options.all():
        # to get the text from the element
        print(option.text_content())

    options.nth(0).click()

    with page.expect_popup() as new_page_info:
        page.get_by_role('button', name='New Tab').click()

    new_page = new_page_info.value  # Get the new tab/page object
    new_page.wait_for_load_state()  # Wait for it to fully load

    print(new_page.title())
    new_page.close()  # Close the new tab

    context.tracing.stop(path = "trace.zip")
    # to close the page
    page.close()
    # to close the browser
    browser.close()

