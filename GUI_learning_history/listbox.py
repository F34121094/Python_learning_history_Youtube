from tkinter import *

def submit():
    a = listbox.get(listbox.curselection())
    print(f"you selected {a}")

def add():
    a = entryBox.get()
    listbox.insert(listbox.size(), a)
    listbox.config(height=listbox.size())
    print(f"food ({a}) just been added to the menu")

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height = listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg = "#f7ffde",
                  font = ("comic sans",20),
                  width = 12,
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"apple")
listbox.insert(3,"banana")
listbox.insert(4,"fried rice")
listbox.insert(5,"stack")
listbox.config(height = listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitbutton = Button(window,text = "submit",
                      command = submit)
submitbutton.pack()

addbutton = Button(window,text = "add",
                      command = add)
addbutton.pack()
deletebutton = Button(window,text = "delete",
                      command = delete)
deletebutton.pack()


window.mainloop()