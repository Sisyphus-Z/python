import json
import os
import time

from selenium import webdriver

import 公共
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
# 最大化浏览器窗口
driver.maximize_window()


def run(url):

    current_dir = os.path.dirname(os.path.abspath(__file__))


    driver.get(url)

    # 使用 WebDriverWait 来等待特定元素的出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/input"))  # 替换为实际元素的 XPath
    )



    # # Step 4: 在新的浏览器窗口中加载cookies
    # with open('cookies.json', 'r') as f:
    #     loaded_cookies = json.load(f)
    #     for cookie in loaded_cookies:
    #         driver.add_cookie(cookie)


    # 从文件中读取 token
    with open(current_dir+'/token.json', 'r') as f:
        token_data = json.load(f)
        token = token_data.get('token', '')

    print("Token:", token)

    driver.execute_script(f"window.localStorage.setItem('token', '{token}');")

    time.sleep(2)
    driver.get(url)

    # driver.refresh()

