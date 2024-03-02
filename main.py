import tts
import stt
import commands.xmldecoder as speak
import commands.ttime.ttime as wtime
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
            for k in speak.timedecoder("date"):
                if k in text:
                    t = time.time()
                    textf = wtime.howdate()
                    tts.say(textf)
                else:
                    continue
            for k in speak.timedecoder("time"):
                if k in text:
                    t = time.time()
                    textf = wtime.howtime()
                    tts.say(textf)
                else:
                    continue
            for k in weather.weatherdecoder():
                if k in text:
                    t = time.time()
                    textf = weather.howweather()
                    tts.say(textf)
                else:
                    continue
            if time.time()-t>=30:
                break