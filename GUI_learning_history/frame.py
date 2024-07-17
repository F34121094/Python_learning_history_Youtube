from tkinter import*

window = Tk()

frame = Frame(window,bg = "pink",bd= 5, relief = SUNKEN)
frame.pack()
button = Button(frame,text = "W",font =("consolas",20),width = 3).pack(side = TOP)
button = Button(frame,text = "A",font =("consolas",20),width = 3).pack(side = LEFT)
button = Button(frame,text = "S",font =("consolas",20),width = 3).pack(side = LEFT)
button = Button(frame,text = "D",font =("consolas",20),width = 3).pack(side = LEFT)


window.mainloop()