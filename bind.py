from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
def clicker(event):
 l=Label(root,text="Mouse position: (%s %s)" % (event.x, event.y))
 l.pack()
 
 return


b=Button(root,text="click me")
b.bind('<Leave>',clicker)
b.pack(pady=20)




root.mainloop()