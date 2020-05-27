from tkinter import *

import random
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")
def pick():
 entries=['Praveen Suthar','Mayank Saini','Google India','Facbook India','Piyush Rathore']
 entries_set=set(entries)
 unique_entries=list(entries_set)
 our_number=len(unique_entries)
 rando=random.randint(0,our_number)
 w_l=Label(root,text=unique_entries[rando],font=('helventica',24))
 w_l.pack(pady=50)
l=Label(root,text="Win-O-Rama!",font=('helventica',24))
l.pack(pady=20)
winB=Button(root,text="PICK OUR WINNER",font=('helventica',24),command=pick)
winB.pack(pady=20)


root.mainloop()