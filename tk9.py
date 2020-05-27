from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')


def open():
  top=Toplevel()
  c=Button(top,text="Destroy Window",command=top.destroy).pack()

b=Button(root,text="Open Second Window",command=open).pack()





root.mainloop()