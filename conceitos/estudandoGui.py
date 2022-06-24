from tkinter import *
root = Tk()
photo = PhotoImage(file='C:\workspace\python\conceitos\computer.gif').subsample(2)
image = Label(master = root, image = photo)
image.pack(side=TOP)
text = Label(master=root, font=("Arial", 18), text="Hello, world!")
text.pack(side=BOTTOM)
root.mainloop()