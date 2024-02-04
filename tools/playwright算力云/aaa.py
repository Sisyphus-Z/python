import subprocess
import time
import pyautogui

import 公共

# 将你想激活的程序的窗口标题传递给函数
window_title = "AutoDl"

global window

def activate_window(window_title):
    global window

    try:
        # 获取所有窗口的标题
        windows = pyautogui.getWindowsWithTitle(window_title)

        # 如果有匹配的窗口，激活它
        if windows:
            print(windows)
            window = windows[0]
            window.activate()
            return True
        else:
            print(f"找不到标题为'{window_title}'的窗口。")
            return False

    except Exception as e:
        print(f"发生错误: {e}")
        return False



def close():
    time.sleep(1)

    activate_window(window_title)

    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')


close()
