from tkinter import *

def click():
    print("you clicked the button!!")

window = Tk()

button = Button(window,
                text = "click here!",
                command = click,
                font = ("Comic Sans", 30),
                )
button.pack()

window.mainloop()