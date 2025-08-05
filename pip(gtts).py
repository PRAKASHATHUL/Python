# PIP - Python package manager


from gtts import gTTS
import os
s=input("Enter your text:")
c=gTTS(s)
c.save("test_audio.mp3")
os.system("start test audio.mp3")

