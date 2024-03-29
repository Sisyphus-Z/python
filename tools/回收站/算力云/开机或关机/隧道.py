import subprocess
import time
import pyautogui

from 公共 import 公共

# 将你想激活的程序的窗口标题传递给函数
window_title = "AutoDl"

def activate_window(window_title):
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




def 打开():
    exe_path = r'D:\AutoDL-SSH-Tools\AutoDL.exe'

    subprocess.Popen(exe_path)

    activate_window(window_title)



    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(0.5)
    # 使用 pyautogui.typewrite 输入用户名
    pyautogui.typewrite(公共.username)
    # 使用 pyautogui.press 模拟按下 Tab 键切换到密码输入框
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.5)

    # 使用 pyautogui.typewrite 输入密码
    pyautogui.typewrite(公共.password)
    time.sleep(1)

    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.5)


    pyautogui.press('space')
    time.sleep(2)

def 关闭():
    try:
        # 获取所有窗口的标题
        windows = pyautogui.getWindowsWithTitle(window_title)

        # 如果有匹配的窗口，激活它
        if windows:
            print(windows)
            window = windows[0]
            window.activate()

            # 模拟按下Alt+F4组合键，关闭窗口
            pyautogui.hotkey('alt', 'f4')
            return True
        else:
            print(f"找不到标题为'{window_title}'的窗口。")
            return False

    except Exception as e:
        print(f"发生错误: {e}")
        return False