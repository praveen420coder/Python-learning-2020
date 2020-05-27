from tkinter import *



root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x400")


#panels
panel1=PanedWindow(bd=4,relief="raised",bg="red")
panel1.pack(fill=BOTH,expand=1)
l=Label(panel1,text="left panel")
panel1.add(l)
panel2=PanedWindow(panel1,orient=VERTICAL,bd=4,relief="raised",bg="blue")
panel1.add(panel2)
top=Label(panel2,text="top Panel")
panel2.add(top)
bottom=Label(panel2,text="Bottom Panel")
panel2.add(bottom)










root.mainloop()