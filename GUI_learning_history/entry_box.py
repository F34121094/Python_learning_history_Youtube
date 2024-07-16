from tkinter import *

def submit():
    username = entry.get()  #entry.get()可以拿到你在entry那個box裡輸入的東西
    print("Hello "+username)

def delete():
    entry.delete(0,END) #不能使用-1，只能用END

def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()

entry = Entry(window,
              font=("Comic Sans",30))
entry.pack(side = "left")

submit_button = Button(window,text ="Submit",
                       command = submit)
submit_button.pack(side = "right")

delete_button = Button(window,text ="Delete",
                       command = delete)
delete_button.pack(side = "right")

backspace_button = Button(window,text ="backspace",
                       command = backspace)
backspace_button.pack(side = "right")

window.mainloop()