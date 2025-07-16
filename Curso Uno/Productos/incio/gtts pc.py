import os
from gtts import gTTS
from random import sample

num=sample(range(0,10),1)

print(num)

hablaMiChavo = 'un pollo come pollo'
tts = gTTS(hablaMiChavo, lang='es')
tts.save('hello.mp3')
os.system('hello.mp3')