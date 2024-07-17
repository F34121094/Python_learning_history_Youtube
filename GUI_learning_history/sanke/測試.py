from tkinter import *

# 创建主窗口
window = Tk()
window.geometry("700x700")
window.title("Centered Frame with Image Background")
window.resizable(False, False)

# 创建 Canvas 并设置背景颜色（可选）
GAME_WIDTH = 700
GAME_HEIGHT = 700
canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack(fill="both", expand=True)

# 设置背景颜色（可选）
canvas.create_rectangle(0, 0, GAME_WIDTH, GAME_HEIGHT, fill="lightblue")

# 创建一个框架并设置背景颜色
frame_width = 300
frame_height = 300
frame = Frame(window, width=frame_width, height=frame_height)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # 将框架放置在窗口中间

# 加载图片
image_path = PhotoImage(file = "back_1_classic.png")  # 替换为你的图片路径


# 在框架中创建一个标签并将图片作为背景
label = Label(frame, image=image_path)
label.place(x=0, y=0, relwidth=1, relheight=1)

# 启动主循环
window.mainloop()