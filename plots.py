from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root=Tk()
root.title("Learn to code")
root.iconbitmap('f:iron.ico')
root.geometry("400x200")

def graph():
  house_prices=np.random.normal(200000,25000,5000)
  plt.pie(house_prices)
  plt.show()

b=Button(root,text="Graph it",command=graph)
b.pack()







root.mainloop()