from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
var=StringVar()
def show():
  l=Label(root,text=var.get())
  l.pack()
c=Checkbutton(root,text="click this box",variable=var,onvalue="on",offvalue="off")
c.deselect()
c.pack()


b=Button(root,text="show selection",command=show)
b.pack()
root.mainloop()