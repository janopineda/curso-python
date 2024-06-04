from gtts import gTTS
from playsound import playsound
import os


rola=os.path.dirname(__file__)
habla=str(os.path.join(rola,"hola.mp3"))
tts=gTTS("Bienvenido a Harkness!.Una preparatoria de excelencia", lang="es")

tts.save(habla)
playsound(habla)