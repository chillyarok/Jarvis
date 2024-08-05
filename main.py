'''core imports'''
from core.stt import listen
from core.tts import say
from core.wake_word_detect import WakeWordDetect
import time

from commands.weather import module as weather
print("good")
while True:
    if WakeWordDetect() == True:
        say("слушаю.")
        t = time.time()
        for text in listen():      
            print(text)
            say(weather.speak(text))
            if time.time()-t>=30:
                break