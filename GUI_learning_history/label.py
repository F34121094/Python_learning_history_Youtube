from tkinter import*
window = Tk()


label_1 = Label(window, text = "Hello, This is my first label program",
              font =("Arial",40,"bold"),
              fg = "red",
              bg = "black",
              relief= "raised",
              bd = 10,
              padx = 20,)
label_1.pack()
label_2 = Label(window, text = "test",
              font =("Arial",40,"bold"),
              fg = "red",
              bg = "black",
              relief= "raised",
              bd = 10,
              padx = 20)
label_2.pack()

window.mainloop()