import keyboard
from selenium.webdriver import Edge, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 用于选择登录端口
from selenium.webdriver.edge.options import Options

import 公共.公共

# 造浏览器配置对象
Edge_op = Options()
# 配置浏览器
# "127.0.0.1:9222"其中，9222是浏览器的运行端口
Edge_op.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 让浏览器带着这个配置运行
driver = Edge(options=Edge_op)

driver.get("https://www.autodl.com/create")
driver.set_window_size(1936, 1056)
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.find_element(By.CSS_SELECTOR, ".region .el-radio-button:nth-child(2) > .el-radio-button__inner").click()
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'j':
        # Drag = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div")  # 找到滚动条
        # print(Drag)
        # Drag.scrollTo(2001,0)

        # 控制滚动条的行为，每次向y轴(及向下)移动10个单位
        # ActionChains(driver).drag_and_drop_by_offset(Drag, 0, 50).perform()

        js='a=document.querySelector("#app > div.create-wrap > div.instance-info > div.card.select-server > div.machine-table > div.loading-box > div > div > div.el-table__body-wrapper.is-scrolling-none");'
        js1='a.scrollTop=a.scrollHeight;'
        result=driver.execute_script(js+js1)


    # 保持程序运行


keyboard.hook(on_key_event)
keyboard.wait('k')  # 等待按下 "esc" 键，你可以根据需要修改
