from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip

from 公共 import 获取页面, 公共
from 公共.公共 import xpath_find

获取页面.run(公共.租url)
driver = 获取页面.driver

地区xpath = "/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div"
xpath_find(driver,地区xpath)
labels = driver.find_elements(By.XPATH, 地区xpath + "/label")
地区数量 = len(labels)

import keyboard
import pyautogui

地区xpath1 = "/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div/label[{}]/span"
地区索引 = 1

数量xpath = "/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[4]/div/div/span"
价格xpath = "/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[9]/div/div/span[1]"
选择点xpath = "/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[1]/div/label/span[1]/span"


def on_key_event(e):
    global 地区索引
    if e.event_type == keyboard.KEY_DOWN and e.name == 'j':

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 地区xpath1.format(地区索引)))  # 替换为实际元素的 XPath
        ).click()

        if 公共.xpath_find(driver,地区xpath1.format(地区索引)).text=="西南A区":
            print("西南A区")
            xpath_find(driver,"/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/div/div[1]/label/span[1]/span").click()
            xpath_find(driver,"/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/div/div[2]/label[2]/span[1]/span").click()




        if 地区索引 < 地区数量:
            地区索引 = 地区索引 + 1
        else:
            地区索引 = 1

        最低价格 = 999.0
        最低价格的i = 1

        i = 1
        while True:
            还剩几台 = int(xpath_find(driver, 数量xpath.format(i)).text)

            if (还剩几台 <= 0):
                time.sleep(0.3)
                xpath_find(driver, 选择点xpath.format(最低价格的i)).click()
                time.sleep(0.3)

                xpath_find(driver,'/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/span').location_once_scrolled_into_view
                break


            价格 = float(WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 价格xpath.format(i)))  # 替换为实际元素的 XPath
            ).text.replace('￥', ''))

            # temp=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr")
            # if(i>=len(temp)):

            xpath_find(driver, 数量xpath.format(i)).location_once_scrolled_into_view
            time.sleep(0.1)



            if 价格 < 最低价格:
                最低价格 = 价格
                最低价格的i = i


            i = i + 1
            xpath_find(driver,数量xpath.format(i))


# 注册回调函数来处理键盘事件
keyboard.hook(on_key_event)

# 保持程序运行
keyboard.wait('k')  # 等待按下 "esc" 键，你可以根据需要修改

# 最终关闭浏览器窗口
driver.quit()
