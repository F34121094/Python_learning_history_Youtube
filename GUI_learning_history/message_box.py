from tkinter import*
from tkinter import messagebox

def click():
    messagebox.showerror(title="this is an info message box",    #title是檔案的名字 message是訊息
                        message="you are a person")

window = Tk()

button = Button(window,command = click,text = "click me")
button.pack()

window.mainloop()