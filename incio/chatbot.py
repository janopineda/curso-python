import os
from random import sample
from gtts import gTTS
from time import sleep

variablerandom=sample(range(0,10),1)
print(variablerandom)
if variablerandom==[1]:
    hablaMiChavo = 'Hola'
    tts = gTTS(text=hablaMiChavo, lang='es')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)
if variablerandom==[2]:
    hablaMiChavo = 'HI'
    tts = gTTS(text=hablaMiChavo, lang='en')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)
if variablerandom==[3]:
    hablaMiChavo = 'bojour'
    tts = gTTS(text=hablaMiChavo, lang='fr')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)
if variablerandom==[4]:
    hablaMiChavo = 'Nǐ hǎo'
    tts = gTTS(text=hablaMiChavo, lang='zh-CN')
    tts.save('hello.mp3')
    os.system('hello.mp3')
    sleep(8)
