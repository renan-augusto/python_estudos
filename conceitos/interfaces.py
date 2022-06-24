from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
  time = strftime('Day: %d %b %Y\nTimes: %H:%M:%Sp\n', localtime())
  showinfo(message=time)

root = Tk()
button = Button(root, text="Clique aqui", command=clicked)
button.pack()
root.mainloop()