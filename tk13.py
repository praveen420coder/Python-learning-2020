from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
def show():
  l=Label(root,text=clicked.get()).pack()



option=["monday","Tuesday","Wednesday","Tuesday"]  
  

clicked=StringVar()
clicked.set(option[0])
drop=OptionMenu(root,clicked,*option)
drop.pack()
b=Button(root,text="Show selection",command=show).pack()
root.mainloop()