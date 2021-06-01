from tkinter import *
import random

root = Tk()
root.geometry("400x400")

def roll():
    dice = ['\u2680','\u2682','\u2683','\u2684','\u2685']
    l1.config(text = f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()

l1=Label(root,font=("Helvetica",260))

b1 = Button(root,text = "Roll the Dice!", foreground = 'blue', command = roll)
b1.place(x = 300, y = 0)
b1.pack()

root.mainloop()