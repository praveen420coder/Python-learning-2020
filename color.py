from tkinter import *
from tkinter import colorchooser


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")

def color():
 my_color=colorchooser.askcolor()[1]
 l=Label(root,text=my_color).pack(pady=10)
 l2=Label(root,text="you picked a color",font=("Helvetica",24),bg=my_color).pack()
b=Button(root,text="pick a color",command=color)
b.pack(pady=10)





root.mainloop()