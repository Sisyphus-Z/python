import tkinter as tk

global 输入
def run():

    def on_button_click(event=None):
        user_input = entry.get()
        global 输入
        输入= user_input
        print("你输入的是：", user_input)
        window.destroy()  # 关闭主窗口

    # 创建主窗口
    window = tk.Tk()
    window.title("关闭界面的UI界面")

    # 创建文本框
    entry = tk.Entry(window)
    entry.pack(pady=10)

    # 创建按钮
    button = tk.Button(window, text="获取输入并关闭", command=on_button_click)
    button.pack()

    # 将回车键绑定到按钮点击事件
    window.bind('<Return>', on_button_click)

    # 启动主循环
    window.lift()  # 提升窗口至顶层
    window.mainloop()
