from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')


my_frame=LabelFrame(root,text="This is my frame",padx=100,pady=100)
my_frame.pack(padx=10,pady=10)

b=Button(my_frame,text="do not click")
b2=Button(my_frame,text="do not click")
b.grid(row=0,column=0)
b2.grid(row=1,column=0)








root.mainloop()