from tkinter import *

import random
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
myLabel=Label(root)
#def mydelete():
 #myLabel.pack_forget()
 #myLabel.grid_forget()
 #myLabel.destroy()
# winB['state']=NORMAL
def myclick():
 global myLabel
 myLabel.destroy()
 hello = "Hello "+e.get()
 myLabel=Label(root,text=hello,font=('helventica',15))
 e.delete(0,END)
 #myLabel.pack(pady=10)
 myLabel.grid(row=3,column=0,pady=10)
 #winB['state']=DISABLED
 
e=Entry(root,width=17,font=('helventica',30))
#e.pack(padx=10,pady=10)
e.grid(row=0,column=0,pady=10,padx=10)

winB=Button(root,text="Enter Your Name",command=myclick)
winB.grid(row=1,column=0,pady=10)
#delB=Button(root,text="Delete Text",command=mydelete)
#delB.grid(row=2,column=0,pady=10)
root.mainloop()