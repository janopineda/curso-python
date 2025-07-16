import os
from random import sample
from gtts import gTTS
from time import sleep
import webbrowser

while True:
    hablaMiChavo = 'Hola, bienvenido a carwash Juan Scutia. selecciona tu servicio' #aqui es donde habla
    tts = gTTS(text=hablaMiChavo, lang='es')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)

    print("Menu")
    print("a) rap de la calle")
    print("b) rap de la carcel")
    print("c) rap de la anexo")
    print("d) rap de la matrix")
    print("e) rap de la goku")

    hablaMiChavo = 'Este es el menú. a rap de calle. b rap de la carcel' #aqui es donde habla
    tts = gTTS(text=hablaMiChavo, lang='es')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)

    opciones=input("Dame la opción")

    if opciones=="a":
        print("este es de la calle")
        webbrowser.open("http://google.com")