from gtts import gTTS
import os

from random import sample 
num=sample(range(0,20),1)
print(num)

if num==[1] :
    tts = gTTS(text='Hola, como estas?',lang="es")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[2]:
    tts = gTTS(text='Hello, How are you?',lang="en")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[3]:
    tts = gTTS(text='Bonjor, Comment ca va?',lang="fr")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[4]:
    tts = gTTS(text='Hallo hoe gaan dit met jou?',lang="af")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[5]:
    tts = gTTS(text='Hej hvordan har du det?',lang="da")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[6]:
    tts = gTTS(text='Hello kamusta ka na?',lang="fil")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[7]:
    tts = gTTS(text='Hallo, wie geht es dir?',lang="de")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[8]:
    tts = gTTS(text='Halo, apa kabarmu?',lang="id")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[9]:
    tts = gTTS(text='Ciao, come stai?',lang="it")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[10]:
    tts = gTTS(text='labas kaip sekasi?',lang="lt")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[11]:
    tts = gTTS(text='Hello apa khabar?',lang="ms")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[12]:
    tts = gTTS(text='Hallo, hvordan har du det?',lang="nb")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[13]:
    tts = gTTS(text='Witam, jak się masz?',lang="pl")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[14]:
    tts = gTTS(text='Olá, como vai?',lang="pt")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[15]:
    tts = gTTS(text='Salut ce mai faci?',lang="ro")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[16]:
    tts = gTTS(text='ahoj ako sa mas?',lang="sk")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[17]:
    tts = gTTS(text='Hej hur mår du?',lang="sv")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[18]:
    tts = gTTS(text='Xin chào bạn khoẻ không?',lang="vi")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[19]:
    tts = gTTS(text='ਹੈਲੋ ਤੁਸੀ ਕਿਵੇਂ ਹੋ?',lang="pa")
    tts.save('hello.mp3')
    os.system("hello.mp3")

if num==[20]:
    tts = gTTS(text='नमस्कार कसा आहेस?',lang="mr")
    tts.save('hello.mp3')
    os.system("hello.mp3")