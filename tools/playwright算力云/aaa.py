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
            for item in windows:
                print(item.title)
                if item.title=="AutoDL":
                    print("关闭"+item.title)
                    window=item
                    window.activate()

            return True
        else:
            print(f"找不到标题为'{window_title}'的窗口。")
            return False

    except Exception as e:
        print(f"发生错误: {e}")
        return False




def open():
    exe_path = 公共.auto_dl_path

    subprocess.Popen(exe_path)

    activate_window(window_title)



    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(0.5)
    # 使用 pyautogui.typewrite 输入用户名
    pyautogui.typewrite(公共.账号)
    # 使用 pyautogui.press 模拟按下 Tab 键切换到密码输入框
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.5)

    # 使用 pyautogui.typewrite 输入密码
    pyautogui.typewrite(公共.密码)
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.2)

    pyautogui.press('tab')
    time.sleep(0.2)


    pyautogui.press('space')
    time.sleep(2)

def close():
    time.sleep(1)

    activate_window(window_title)

    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')

close()