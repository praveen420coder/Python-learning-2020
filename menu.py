from tkinter import *



root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
my_menu=Menu(root)
root.config(menu=my_menu)
def our_command():
   
   l = Label(root, text="Do nothing button")
   l.pack()
def edit_command():
    hide()
    new_frame1.pack(fill="both",expand=1) 
    l = Label(new_frame1, text="Do nothing button")
    l.pack()
def hide():
 for widget in new_frame.winfo_children():
  widget.destroy()
 for widget in new_frame1.winfo_children():
  widget.destroy() 
 new_frame.pack_forget()
 new_frame1.pack_forget()
def new_command():
 hide()
 new_frame.pack(fill="both",expand=1)
 l = Label(new_frame, text="Do nothing button")
 l.pack()
#create a menu items
file_menu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New..",command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
editmenu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut", command=edit_command)
editmenu.add_command(label="Copy", command=our_command)


new_frame=Frame(root,width=400,height=400,bg="#9c27b0")
new_frame1=Frame(root,width=400,height=400,bg="red")

root.mainloop()