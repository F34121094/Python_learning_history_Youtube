from tkinter import *

def openfile():
    print("the file has been opened")
def save():
    print("the file has been saved")

window = Tk()

menubar = Menu(window)
window.config(menu = menubar)

fileMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File",menu= fileMenu)
fileMenu.add_command(label = "Open", command = openfile)
fileMenu.add_command(label = "Save",command = save)
fileMenu.add_separator()    #separator可以在bar之間加一個橫線
fileMenu.add_command(label = "Exit",command = quit)

window.mainloop()