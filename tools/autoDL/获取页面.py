import json
import time

from selenium import webdriver

import 公共
import 用户输入
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
# 最大化浏览器窗口
driver.maximize_window()


def run():

    driver.get(公共.url)




    time.sleep(2)

    # # Step 4: 在新的浏览器窗口中加载cookies
    # with open('cookies.json', 'r') as f:
    #     loaded_cookies = json.load(f)
    #     for cookie in loaded_cookies:
    #         driver.add_cookie(cookie)

    # 从文件中读取 token
    with open('token.json', 'r') as f:
        token_data = json.load(f)
        token = token_data.get('token', '')

    print("Token:", token)

    driver.execute_script(f"window.localStorage.setItem('token', '{token}');")

    time.sleep(2)
    driver.get(公共.url)

    # driver.refresh()

