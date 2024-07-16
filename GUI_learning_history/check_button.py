from tkinter import*
def display():
    if (x.get() == 1):
        print("Agree!")
    else:
        print("Don't agree!")

window = Tk()
window.geometry("420x100")
x = IntVar()

check_button = Checkbutton(window,
                           text = "I agree this",
                           variable=x,  #variable變量設定在打勾為invalue的值，沒有打勾設定在offvalue的值
                           onvalue = 1,
                           offvalue = 0,
                           command = display,
                           font = ("Comic sans",30),
                           padx = 10,
                           pady = 5)
check_button.pack()

window.mainloop()