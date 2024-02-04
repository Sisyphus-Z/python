from playwright.sync_api import Playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        channel="msedge",
        headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True, storage_state="state.json")
    page = context.new_page()
    page.goto("https://www.autodl.com/create")


    js = 'a=document.querySelector("#app > div.create-wrap > div.instance-info > div.card.select-server > div.machine-table > div.loading-box > div > div > div.el-table__body-wrapper.is-scrolling-none");'
    js1 = 'a.scrollTop=a.scrollHeight;'
    page.evaluate(js + js1)