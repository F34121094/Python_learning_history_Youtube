from tkinter import*

def submit():
    print(f"current temperature is : {scale.get()}C")

window = Tk()

scale = Scale(window,from_= 100,to = 0,#記得起始點的指令為from_
              length = 400,
              font = ("comic sans",10),
              tickinterval = 10 #讓他每10個單位顯示一次

             )


scale.pack()

button = Button(window,text = "submit",command = submit)
button.pack()
window.mainloop()