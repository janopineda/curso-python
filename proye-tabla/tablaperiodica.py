
import serial
import time
from gtts import gTTS
import os
from playsound import playsound


x = 0
arduino = serial.Serial('COM4', 9600)

while True:
    time.sleep(0.5)
    dato = arduino.readline()
    decoded_var = dato.decode('utf-8', errors='ignore').strip()  
    print("Variable en uso: ", decoded_var)

    if decoded_var == "Fosforo":
        texto = "Fosforo mi chavo"
        tts = gTTS(text=texto, lang='es')

        tts.save("voz.mp3")
        playsound("voz.mp3")
        time.sleep(2)

    if decoded_var == "Magnecio":
        texto = "Magnecio sipirili"
        tts = gTTS(text=texto, lang='es')
        
        tts.save("voz.mp3")
        playsound("voz.mp3")
        time.sleep(2)

arduino.close()
