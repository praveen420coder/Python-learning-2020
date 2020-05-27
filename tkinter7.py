from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
#r=IntVar()
#r.set(2)
modes=[

   ("peparroni","peparroni"),
   ("cheese","cheese"),
   ("mushroom","mushroom"),
   ("mix","mix"),
   ("double","double")



]
pizza=StringVar()
pizza.set("peparroni")

def clicked(value):
  l=Label(root,text=value).pack()

for text,mode in modes:
  Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

#Radiobutton(root,text="Option1",variable=r,value=1).pack()
#Radiobutton(root,text="Option2",variable=r,value=2).pack()
#Radiobutton(root,text="Option3",variable=r,value=3).pack()

l=Label(root,text=pizza.get()).pack()





b=Button(root,text="Click me",command=lambda: clicked(pizza.get())).pack()
root.mainloop()