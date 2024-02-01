from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip


from 公共 import 获取页面, 公共

获取页面.run(公共.租url)
driver = 获取页面.driver


import keyboard
import pyautogui

地区xpath="/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div"
地区xpath1="/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div/label[{}]/span"
地区索引=1



数量xpath= "/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[4]/div/div/span"
价格xpath="/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[9]/div/div/span[1]"
选择点xpath="/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[{}]/td[1]/div/label/span[1]/span"
def on_key_event(e):
    global 地区索引
    if e.name == 'j':

        # 设置显式等待，等待最多10秒，每0.5秒检查一次条件
        wait = WebDriverWait(driver, 10, poll_frequency=0.5)
        labels = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, 地区xpath)))
        地区数量=len(labels)

        print(地区数量)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 地区xpath1.format(地区索引)))  # 替换为实际元素的 XPath
        ).click()

        if 地区索引<地区数量:
            地区索引=地区索引+1
        else:
            地区索引=1


        最低价格=999.0
        最低价格的i=1



        i=1
        还剩几台=999
        while 还剩几台>0:
            还剩几台 = int(WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 数量xpath.format(i)))  # 替换为实际元素的 XPath
            ).text)


            价格 = float(WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 价格xpath.format(i)))  # 替换为实际元素的 XPath
            ).text.replace('￥', ''))



            if 价格<最低价格:
                最低价格=价格
                最低价格的i=i

            i=i+1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 选择点xpath.format(最低价格的i)))  # 替换为实际元素的 XPath
        ).click()




# 注册回调函数来处理键盘事件
keyboard.hook(on_key_event)

# 保持程序运行
keyboard.wait('esc')  # 等待按下 "esc" 键，你可以根据需要修改






# 最终关闭浏览器窗口
driver.quit()
