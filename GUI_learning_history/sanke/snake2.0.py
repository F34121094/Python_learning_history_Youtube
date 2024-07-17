from tkinter import*
import random
from tkinter import messagebox

def generate_main_menu():
    global frame_main_menu
    frame_main_menu = Frame(window)
    frame_main_menu.place(x=190, y=350)
    button = Button(frame_main_menu, text="Start !", font=("Arial", 25), width=17, command=game_start).pack()
    button = Button(frame_main_menu, text="Change background", font=("Arial", 25), width=17,
                    command=change_background).pack()
    button = Button(frame_main_menu, text="Feedback", font=("Arial", 25), width=17,
                    command=feedback).pack()  # feedback功能完成
    return

def game_start():
    global high_score
    def again():
        buttom_back.destroy()
        buttom_continue.destroy()
        buttom_exit.destroy()
        game_start()

    global back_num
    frame_main_menu.destroy()
    SPEED = 50
    SPACE_SIZE = 50
    BODY_PARTS = 3
    SNAKE_COLOR = "#00FF00"
    FOOD_COLOR = "#FF0000"
    if back_num == 0: new_background = PhotoImage(file="back_1_classic.png")  # 載入新的背景
    elif back_num == 1: new_background = PhotoImage(file="back_2_grass.png")
    elif back_num == 2: new_background = PhotoImage(file="back_3_ocean.png")
    elif back_num == 3: new_background = PhotoImage(file="back_4_volcano.png")
    elif back_num == 4: new_background = PhotoImage(file="back_5_starry.png")
    elif back_num == 5: new_background = PhotoImage(file="back_6_y2k.png")
    canvas.delete("all")  # 先刪除現在的背景
    canvas.create_image(0, 0, image = new_background, anchor="nw")
    canvas.image = new_background
    #改完背景
    class Snake:

        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

    class Food:

        def __init__(self):
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
    def next_turn(snake, food):

        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:

            global score

            score += 1

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        if check_collisions(snake):
            game_over()

        else:
            window.after(SPEED, next_turn, snake, food)

    def change_direction(new_direction):
        global direction
        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    def check_collisions(snake):

        x, y = snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over():
        global high_score
        if score > high_score:
            high_score = score
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 5,font=('consolas', 70),
                           text="GAME OVER", fill="red", tag="gameover",anchor="n")
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2.5,font=('consolas', 40),
                           text=f"your score : {score}", fill="gray", tag="gameover",anchor="n")
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 35),
                           text=f"highest score : {high_score}", fill="gray", tag="gameover", anchor="n")
        global buttom_back,buttom_continue,buttom_exit
        buttom_back = Button(window,text = "Main menu",font = ("Arial",20),command = game_over_back)
        buttom_back.place(x = 264, y = 520)
        buttom_continue = Button(window, text="Play again", font=("Arial", 20), command=again)
        buttom_continue.place(x=270, y=450)
        buttom_exit = Button(window, text="Exit", font=("Arial", 20), command=Exit)
        buttom_exit.place(x=310, y=590)

    global score
    score = 0
    global direction
    direction = 'down'

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction('left'))   #bind為鍵盤輸入指示
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)

def change_background():
    global back_num
    back_num = 0
    def background_select():
        global frame
        global text_label
        frame = Frame(window, width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        if back_num == 0:
            text_label = Label(window,text ="classic background",font = ("Arial",16),bg ="white")
            text_label.place(x = 261,y = 150)
            back_image = PhotoImage(file = "back_1_classic.png")
            frame.back_image = back_image
            label = Label(frame,image = back_image)
            label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        elif back_num == 1:
            text_label = Label(window, text="grass land", font=("Arial", 16), bg="white")
            text_label.place(x=298, y=150)
            back_image = PhotoImage(file="back_2_grass.png")
            frame.back_image = back_image
            label = Label(frame, image=back_image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
        elif back_num == 2:
            text_label = Label(window, text="ocean", font=("Arial", 16), bg="white")
            text_label.place(x=315, y=150)
            back_image = PhotoImage(file="back_3_ocean.png")
            frame.back_image = back_image
            label = Label(frame, image=back_image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
        elif back_num == 3:
            text_label = Label(window, text="volcano", font=("Arial", 16), bg="white")
            text_label.place(x=310, y=150)
            back_image = PhotoImage(file="back_4_volcano.png")
            frame.back_image = back_image
            label = Label(frame, image=back_image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
        elif back_num == 4:
            text_label = Label(window, text="starry night", font=("Arial", 16), bg="white")
            text_label.place(x=294, y=150)
            back_image = PhotoImage(file="back_5_starry.png")
            frame.back_image = back_image
            label = Label(frame, image=back_image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
        elif back_num == 5:
            text_label = Label(window, text="y2k", font=("Arial", 16), bg="white")
            text_label.place(x=330, y=150)
            back_image = PhotoImage(file="back_6_y2k.png")
            frame.back_image = back_image
            label = Label(frame, image=back_image)
            label.place(x=0, y=0, relwidth=1, relheight=1)

    background_select()
    def left():
        global back_num
        back_num -= 1
        if back_num < 0: back_num = 5
        frame.destroy()
        text_label.destroy()
        background_select()
    def right():
        global back_num
        back_num += 1
        if back_num > 5: back_num = 0
        frame.destroy()
        text_label.destroy()
        background_select()
    def back():
        new_background = PhotoImage(file="BackGround.png")  # 載入新的背景
        canvas.delete("all")  # 先刪除現在的背景
        canvas.create_image(0, 0, image=new_background, anchor="nw")
        canvas.image = new_background
        back_button.destroy()
        left_button.destroy()
        right_button.destroy()
        confirm_button.destroy()
        frame.destroy()
        text_label.destroy()
        global frame_main_menu  # 使用全局变量来重新生成主菜单
        frame_main_menu.destroy()
        generate_main_menu()
        return
    frame_main_menu.destroy()
    new_background = PhotoImage(file="just_BackGround.png") #載入新的背景
    canvas.delete("all")  # 先刪除現在的背景
    canvas.create_image(0, 0, image=new_background, anchor="nw")
    canvas.image = new_background
    back_button = Button(window,text="back",font = ("arial",15),command = back)
    back_button.place(x = 20,y = 20)
    left_button = Button(window,text ="<",font = ("arial",15),command = left)
    left_button.place(x = 30, y = 320)
    right_button = Button(window, text=">", font=("arial", 15), command=right)
    right_button.place(x = 640, y = 320)
    confirm_button = Button(window, text="confirm", font=("arial", 15),padx = 20, command=back)
    confirm_button.place(x=288, y=600)
def feedback(): #已完成
    def feedback_print():
        print(text.get("1.0",END))
    feedback_window = Toplevel()
    feedback_window.title("Feedback message area")
    feedback_window.geometry("300x300")
    feedback_window.resizable(False,False)
    text = Text(feedback_window, height = 13, width = 30)
    text.pack(pady = 20, padx = 10)
    button_fe = Button(feedback_window,text = "submit",command=feedback_print,padx = 10).pack(side = "bottom")

def game_over_back():   #已完成
    new_background = PhotoImage(file="BackGround.png")  # 載入新的背景
    canvas.delete("all")  # 先刪除現在的背景
    canvas.create_image(0, 0, image=new_background, anchor="nw")
    canvas.image = new_background
    buttom_back.destroy()
    buttom_continue.destroy()
    buttom_exit.destroy()
    generate_main_menu()

def Exit(): #已完成
    if messagebox.askokcancel(title = "confirmation",message="Are you going to exit ?\n(the score would be delete)"):
        window.destroy()
    else:
        return

global back_num
back_num = 0
GAME_WIDTH = 700
GAME_HEIGHT = 700

window = Tk()
window.geometry("700x700")
global high_score
high_score = 0
#--------------------------------------------------------------  主選單區
background = PhotoImage(file="BackGround.png")
canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack(fill="both", expand=True)

# 在Canvas上放置背景图片
canvas.create_image(0, 0, image=background, anchor="nw")

window.title("Snake game")
window.resizable(False,False)

generate_main_menu()
#--------------------------------------------------------------

window.mainloop()