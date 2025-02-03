from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    label = Label(top, text = "This is toplevel window")
    label.pack()
    top.mainloop()

label2 = Label(root, text = "This is root window")
button = Button(root, text = "Click here to open another window", command = topwin)
label2.pack()
button.pack()

root.mainloop()