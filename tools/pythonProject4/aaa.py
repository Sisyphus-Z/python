import time

import keyboard
from queue import Queue

# 创建一个队列
my_queue = Queue()

# 定义一个回调函数，当按下 'j' 键时调用
def add_element_to_queue():
    # 在队列中添加元素，可以是任何你想要的值
    my_queue.put("New Element Added")

# 使用 add_hotkey 注册回调函数，指定按下 'j' 键时调用
keyboard.add_hotkey('j', add_element_to_queue)


while True:
    time.sleep(2)
    my_queue.get()
    print(1111)

# 运行主循环，保持程序运行
keyboard.wait('esc')  # 等待按下 'esc' 键退出程序
