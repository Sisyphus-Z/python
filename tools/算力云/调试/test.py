import keyboard
from selenium.webdriver import Edge
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
web = Edge(options=Edge_op)


def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'j':
        # print(web.find_elements(By.CLASS_NAME, "table__body-wrapper"))
        # print(web.find_element(By.CLASS_NAME,"table__body-wrapper"))
        l=web.find_elements(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/div/div/div[3]/table/tbody/tr')
        print(len(l))

keyboard.hook(on_key_event)

# 保持程序运行
keyboard.wait('k')  # 等待按下 "esc" 键，你可以根据需要修改
