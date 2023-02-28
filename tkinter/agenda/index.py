import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Agenda")

etiQue=customtkinter.CTkLabel(master=app,text="Bienvenido")
etiQue.place(x=190,y=10)
userP=customtkinter.CTkEntry(master=app,placeholder_text="Usuario")
userP.place(x=150,y=60)
pasw=customtkinter.CTkEntry(master=app,placeholder_text="Contraseña")
pasw.place(x=150,y=100)
button = customtkinter.CTkButton(master=app, text="Entrar", )
button.place(x=150,y=140)
app.mainloop()