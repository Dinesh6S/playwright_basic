from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://demoqa.com/frames")


    frame = page.frame(name="frame1")  


    text = frame.locator("h1").text_content()
    print("Text inside iframe:", text)

    browser.close()
