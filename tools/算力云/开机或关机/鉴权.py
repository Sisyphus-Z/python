import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from 公共 import 公共

# 初始化一个浏览器对象
driver = webdriver.Edge()

# Step 1: 登录网站获取鉴权信息
driver.get(公共.控制台url)
# 在这里执行登录操作，填写用户名和密码等

# Step 2: 输入用户名和密码
# 使用 WebDriverWait 来等待用户名输入框的出现
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/input"))
)  # 请替换为实际的用户名输入框的XPath表达式

# 使用 WebDriverWait 来等待密码输入框的出现
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/form/div[3]/div/div/input"))
)  # 请替换为实际的密码输入框的XPath表达式

# 在这里输入你的用户名和密码
username_input.send_keys("18694044791")
password_input.send_keys("12@Qwertyu")

# 找到登录按钮并点击
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/form/div[4]/div/button[1]")  # 请替换为实际的登录按钮的属性
login_button.click()

time.sleep(2)

# # Step 2: 获取当前会话的所有cookies
# cookies = driver.get_cookies()
# # Step 3: 将cookies保存到JSON文件中，以便后续使用
# with open('cookies.json', 'w') as f:
#     json.dump(cookies, f)

while True:
    # 使用 JavaScript 获取本地存储中的 token
    token = driver.execute_script("return window.localStorage.getItem('token');")
    if(token != None):
        break

# 保存 token 到 JSON 文件
token_data = {'token': token}
with open('../公共/token.json', 'w') as f:
    json.dump(token_data, f)


# 关闭当前浏览器窗口
driver.quit()


