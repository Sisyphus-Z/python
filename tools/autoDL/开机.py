from selenium.common import WebDriverException

import 获取页面
import 用户输入
import json
import time

from selenium import webdriver

import 公共
import 用户输入
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

获取页面.run()
driver=获取页面.driver

# 在这里进行后续操作
输入 = 用户输入.run()
if 输入!="":
    开机="/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[3]/table/tbody/tr[{}]/td[10]/div/div/button/span".format(输入)

    # 使用 WebDriverWait 来等待特定元素的出现
    element_to_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 开机))  # 替换为实际元素的 XPath
    )

    # 点击元素
    element_to_click.click()

    # 使用 WebDriverWait 来等待特定元素的出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[65]/div/div[3]/button[2]/span"))  # 替换为实际元素的 XPath
    ).click()


# 最终关闭浏览器窗口
driver.quit()