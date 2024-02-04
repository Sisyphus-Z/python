from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge",headless=False,args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()


    page.goto("https://www.autodl.com/login?url=/console/instance/list")


    page.get_by_placeholder("请输入手机号").click()
    page.get_by_placeholder("请输入手机号").fill("18694044791")
    page.get_by_placeholder("请输入手机号").press("Tab")
    page.get_by_placeholder("请输入密码").fill("12@Qwertyu")
    page.get_by_role("button", name="登录", exact=True).click()

    page.wait_for_timeout(2000)

    # local_storage_data = page.evaluate("() => { return JSON.stringify(localStorage); }")

    storage = context.storage_state(path="state.json")

    page.wait_for_timeout(1000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

