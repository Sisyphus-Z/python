from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip

import 隧道
import 用户输入

用户输入.run()
from 公共 import 获取页面, 公共

获取页面.run(公共.控制台url)
driver = 获取页面.driver



# 在这里进行后续操作
if 用户输入.输入 != "":
    开机或关机 = "/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[3]/table/tbody/tr[{}]/td[10]/div/div/button/span".format(
        用户输入.输入)
    # 使用 WebDriverWait 来等待特定元素的出现
    span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 开机或关机))  # 替换为实际元素的 XPath
    )
    span.click()
    span_content = span.text

    # 使用 WebDriverWait 来等待特定元素的出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[65]/div/div[3]/button[2]/span"))  # 替换为实际元素的 XPath
    ).click()

    if span_content == "开机":

        复制账号与密码="/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[3]/table/tbody/tr[{}]/td[8]/div/div/div/div[{}]/span[2]"
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            复制账号与密码.format(用户输入.输入, 2)))
            # 替换为实际元素的 XPath
        ).click()
        time.sleep(0.5)
        公共.username=pyperclip.paste()
        time.sleep(0.5)


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            复制账号与密码.format(用户输入.输入, 4)))
            # 替换为实际元素的 XPath
        ).click()
        time.sleep(0.5)
        公共.password=pyperclip.paste()
        time.sleep(0.5)

        隧道.打开()
    else:
        隧道.关闭()




# 最终关闭浏览器窗口
driver.quit()
