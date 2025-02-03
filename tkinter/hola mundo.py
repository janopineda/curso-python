from tkinter import *
root=Tk()
root.title("hola")
root.geometry("400x400")

texto=Label(root,text="¡Hola Mundo!")
texto.pack()

entrada=Entry(root)
entrada.pack()
root.mainloop()