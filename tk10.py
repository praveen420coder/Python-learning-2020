from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')



def open():
  global i
  root.filename = filedialog.askopenfilename(initialdir="F:/image",title="select a file",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
  l=Label(root,text=root.filename).pack()
  i=ImageTk.PhotoImage(Image.open(root.filename))
  ml=Label(image=i).pack()
  
b=Button(root,text="open File",command=open).pack()
root.mainloop()