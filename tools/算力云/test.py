import keyboard

def on_key_event(e):
    if e.name == 'j':
        print("你按下了 'j' 键！")

# 注册回调函数来处理键盘事件
keyboard.hook(on_key_event)

# 保持程序运行
keyboard.wait('esc')  # 等待按下 "esc" 键，你可以根据需要修改
