from time import *
from tkinter import *

x=0
def contar ():
    for x in range(1,11):
    #print(x)
        second.config(text=x)
        sleep(1)
        root.update()

root=Tk()
root.geometry("500x500")
second=Label(root,text=x)
second.configure(font="Arial 300")
second.pack()
bt=Button(root, text="contar",width=50, height=100,background="#18BCAD", command=contar)
bt.configure(font="Arial 22")
bt.pack()

mainloop()