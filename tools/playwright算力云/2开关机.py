import time

import keyboard
import pyperclip
from playwright.sync_api import Playwright, sync_playwright, expect
from queue import Queue

import 公共
import 隧道


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        channel="msedge",
        headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True, storage_state="state.json")

    page = context.new_page()

    page.goto("https://www.autodl.com/console/instance/list")

    # page.pause()

    while True:
        temp = queue.get()
        print("循环")

        if temp.isdigit():

            开关机按钮 = page.locator(
                "//html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[3]/table/tbody/tr[{}]/td[10]/div/div/button/span".format(
                    temp))
            开关机 = 开关机按钮.text_content()

            开关机按钮.click()

            page.get_by_role("button", name="确定").click()

            print(开关机)

            global 是否放入queue
            是否放入queue = False

            if ("开机" in 开关机):
                print("1111")

                page.get_by_role("cell", name="登录指令 ssh").locator("span").nth(1).click()
                公共.账号 = pyperclip.paste()

                page.get_by_role("cell", name="登录指令 ssh").locator("span").nth(3).click()
                公共.密码 = pyperclip.paste()

                隧道.open()

            elif ("关机" in 开关机):
                print("2222")
                隧道.close()

            是否放入queue = True

        page.wait_for_timeout(1000)


queue = Queue(maxsize=1)
last_put_time = 0
是否放入queue = True


def temp1(e):
    if e.event_type == keyboard.KEY_DOWN and 是否放入queue == True:
        # if(not queue.empty()):
        #     queue.get_nowait()

        global last_put_time
        current_time = time.time()

        if current_time - last_put_time >= 1:
            queue.put(e.name)
            last_put_time = current_time
            print(f"成功放入队列: {e.name}")


keyboard.hook(temp1)

with sync_playwright() as playwright:
    run(playwright)
