from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')

#showinfo,show warning,show error,ask question,askesno,askokcancel
def popup():
 response=messagebox.askquestion("This is my popup","Hello world")
 Label(root,text=response).pack()
 if response=="yes":
   Label(root,text="yuo click yes").pack()
 else:
    Label(root,text="yuo click no").pack()

b=Button(root,text="poppup",command=popup).pack()






root.mainloop()