from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")

v=Scale(root,from_=0,to=200)
v.pack()


h=Scale(root,from_=0,to=200,orient=HORIZONTAL)
h.pack()

#l=Label(root,text=h.get()).pack()

def slide():
 l=Label(root,text=h.get()).pack()
 root.geometry(str(h.get())+"x"+str(v.get()))
b=Button(root,text="Click me",command=slide).pack()
root.mainloop()