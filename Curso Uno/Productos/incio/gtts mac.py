import subprocess
from gtts import gTTS


hablaMiChavo = 'un pollo come pollo'
tts = gTTS(hablaMiChavo, lang='es')
tts.save('hello.mp3')
subprocess.run(['afplay', 'hello.mp3'])