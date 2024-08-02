'''core imports'''
from core.stt import listen
from core.tts import say
from core.wake_word_detect import WakeWordDetect
import time

from commands.weather.module import speak
print("good")
while True:
    if WakeWordDetect() == True:
        say("слушаю.")
        t = time.time()
        for text in listen():      
            print(text)
            try:
                say(speak(text))
            except:
                pass
            if time.time()-t>=30:
                break