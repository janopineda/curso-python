from PIL import Image,ImageTk
import tkinter as tk

root = tk.Tk()
imagen = ImageTk.PhotoImage(Image.open("C:\Users\LETICIA\Desktop\tkinter\meme.png"))
fondo = tk.Label(root,image = imagen)
fondo.pack() #Se ubica la imagen de fundo
root.mainloop()