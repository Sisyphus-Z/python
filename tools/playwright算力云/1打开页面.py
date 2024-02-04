import keyboard
from playwright.sync_api import Playwright, sync_playwright, expect
from queue import Queue

l = [
    "西北B区:RTX A4000,RTX 3060",
    "北京A区:RTX 2080,RTX 3080,RTX A4000",
    "内蒙A区:TITAN Xp"
]


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        channel="msedge",
        headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True, storage_state="state.json")

    page = context.new_page()

    page.goto("https://www.autodl.com/create")



    my_queue = Queue()

    def temp1(e):
        if e.event_type == keyboard.KEY_DOWN and (e.name == 'j' or e.name=="k"):
            my_queue.put(e.name)
    keyboard.hook(temp1)



    index = -1
    while True:
        # event = keyboard.read_event(suppress=True)
        #
        # pressed_key = keyboard.wait((ord('j'), ord('k')))
        # print(1)
        key=my_queue.get()

        # b=False

        if key=='j':
            index = index + 1
        elif key=='k':
            index = index - 1

        if index >= len(l):
            index = index-len(l)
        elif index<0:
            index =index +len(l)

        # if b==True:
        地区 = l[index].split(":")[0]
        机器列表 = l[index].split(":")[1].split(",")
        page.locator("label").filter(has_text=地区).click()
        for item in 机器列表:
            page.locator("label").filter(has_text=item).locator("span").nth(1).click()





with sync_playwright() as playwright:
    run(playwright)
