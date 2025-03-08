from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    context.tracing.start(screenshots = True, snapshots= True, sources = True)

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


    def handle_alert(dialog):
        print(f"Alert Message: {dialog.message}")  # Print the alert text
        # dialog.accept()  # Clicks "OK"
        dialog.accept("Hello Playwright!") 

    options.nth(1).click()
    page.on("dialog", handle_alert)

    # page.locator('//button[@id="confirmButton"]').click()



    page.locator('//button[@id="promtButton"]').click()


    page.wait_for_timeout(2000)  # Wait to observe
    # with page.expect_event("dialog") as dialog_info:
    #     page.locator('//button[@id="alertButton"]').click()
    # dialog = dialog_info.value
    # print(dialog.message)  # Prints alert message
    # dialog.accept()  # Clicks "OK"