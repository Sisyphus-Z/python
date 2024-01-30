import pyautogui
import time

# 切换到指定窗口（假设窗口标题为 "Your Window Title"）
window_title = "AutoDl"
pyautogui.getWindowsWithTitle(window_title)[0].activate()

# 等待一段时间确保窗口激活
time.sleep(1)

# 输入用户名和密码
username = "your_username"
password = "your_password"

# 使用 pyautogui.typewrite 输入用户名
pyautogui.typewrite(username)
# 使用 pyautogui.press 模拟按下 Tab 键切换到密码输入框
pyautogui.press('tab')
# 使用 pyautogui.typewrite 输入密码
pyautogui.typewrite(password)

# 你可以继续模拟其他键盘操作，例如按下 Enter 键来提交登录表单
# pyautogui.press('enter')
