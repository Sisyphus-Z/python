import pygetwindow as gw

def get_all_windows_titles():
    try:
        # 获取所有窗口的标题
        window_titles = gw.getAllTitles()

        return window_titles

    except Exception as e:
        print(f"发生错误: {e}")
        return []

# 获取所有窗口的标题
all_window_titles = get_all_windows_titles()

# 打印窗口标题
for title in all_window_titles:
    print(title)
