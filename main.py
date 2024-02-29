import tts
import stt
import commands.xmldecoder as speak
import commands.time.ttime as wtime
import wake_word_detect as wwd
import commands.weather.weather as weather
import random


print("good")
while True:
    if wwd.WakeWordDetect() == True:
        tts.say("слушаю.")
        for text in stt.listen():      
            print(text)
            if text in str(speak.speakkommand().keys()):
                textf = speak.speakkommand()[text][random.randint(0,len(speak.speakkommand()[text])-1)]
                tts.say(textf)
            for k in speak.timedecoder("date"):
                if k in text:
                    textf = wtime.howdate()
                    tts.say(textf)
                else:
                    continue
            for k in speak.timedecoder("time"):
                if k in text:
                    textf = wtime.howtime()
                    tts.say(textf)
                else:
                    continue
            for k in weather.weatherdecoder():
                if k in text:
                    textf = weather.howweather()
                    tts.say(textf)
                else:
                    continue