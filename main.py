import tts
import stt
import commands.xmldecoder as speak
import commands.time.whattime as wtime
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
            if speak.timedecoder("date") in text:
                textf = wtime.howdate()
                tts.say(textf)
            if speak.timedecoder("time") in text:
                  textf = wtime.howtime()
                  tts.say(textf)
            if "какая сейчас погода" in text:
                textf = weather.howweather()
                tts.say(textf)