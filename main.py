import tts
import stt
import commands.xmldecoder as speak
import commands.time.whattime as wtime
import wake_word_detect as wwd
import commands.weather.weather as weather
import random
import time


print("good")
while True:
    if wwd.WakeWordDetect() == True:
        tts.say("слушаю.")
        t = time.time()
        for text in stt.listen():      
            print(text)
            if text in str(speak.speakkommand().keys()):
                t = time.time()
                textf = speak.speakkommand()[text][random.randint(0,len(speak.speakkommand()[text])-1)]
                tts.say(textf)
            if speak.timedecoder("date") in text:
                t = time.time()
                textf = wtime.howdate()
                tts.say(textf)
            if speak.timedecoder("time") in text:
                  t = time.time()
                  textf = wtime.howtime()
                  tts.say(textf)
            if "какая сейчас погода" in text:
                t = time.time()
                textf = weather.howweather()
                tts.say(textf)
            if time.time()-t>30 or "пока" in text:
                print(2)
                break