from tkinter import*

food = ["pizza","hamburger","hotdog"]

def order():
    if (x.get()==0):
        print("you order a pizza")
    elif (x.get() == 1):
        print("you order a hamburger")
    else:
        print("you order a hotdog")

window = Tk()
x = IntVar()    #x為一個整能存放 int 的變數
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index],
                              variable = x,     #所有的標籤共用一個x值，所以當其他的被選中時，其他的就會被取消選定
                              value = index,    #value值為當前的index，負責將值傳給x
                              padx = 25,
                              font = ("comic sans",20),
                              indicatoron = 0,
                              command = order
                              )
    radiobutton.pack()

window.mainloop()