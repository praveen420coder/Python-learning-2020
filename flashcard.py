from tkinter import *
from PIL import ImageTk,Image
from random  import randint


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
#create state flash card function
def states():
 hide() 
 state_frame.pack(fill=BOTH,expand=1)
 #my_label=Label(state_frame,text="States").pack()
 our_states=['california','la','newyork','texas']
 
 rando=randint(0,len(our_states)-1)
 state="f:/new/"+our_states[rando]+ ".png"
 global state_image
 state_image=ImageTk.PhotoImage(Image.open(state))
 show_state=Label(state_frame,image=state_image)
 show_state.pack(pady=15)
 
def state_capital():
 hide()
 state_capital_frame.pack(fill=BOTH,expand=1)
 #my_label=Label(state_capital_frame,text="Capitals").pack()
 
 
 
 
 
 
 
 
 
 
 
def hide():


 for widget in state_frame.winfo_children():
  widget.destroy()
 for widget in state_capital_frame.winfo_children():
  widget.destroy()
 state_frame.pack_forget()
 state_capital_frame.pack_forget()









my_menu=Menu(root)
root.config(menu=my_menu)


stats_menu=Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=stats_menu)
stats_menu.add_command(label="States",command=states)
stats_menu.add_command(label="State Capitals",command=state_capital)
stats_menu.add_separator()
stats_menu.add_command(label="Exit",command=root.quit)

state_frame=Frame(root,width=500,height=500)
state_capital_frame=Frame(root,width=500,height=500)

root.mainloop()