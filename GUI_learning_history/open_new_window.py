from tkinter import*

def create_window():
    new_window = Toplevel()

window = Tk()

Button(window, text = "create new window", command = create_window,width = 30).pack()

window.mainloop()