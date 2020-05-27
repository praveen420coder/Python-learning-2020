from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")

class Elder:
 def __init__(self,master):
  myFrame=Frame(master)
  myFrame.pack()
  
  self.b=Button(master,text="click me",command=self.clicker)
  self.b.pack(pady=20)

 def clicker(self):
  print("Look at you you clicked")



e=Elder(root)




root.mainloop()