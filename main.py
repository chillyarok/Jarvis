import tts
import stt
import commands.xmldecoder as speak
import wake_word_detect as wwd
import random
import time


print("good")
while True:
    if wwd.WakeWordDetect() == True:
        print(1)
        t = time.time()
        for text in stt.listen():      
            print(t)
            print(int(time.time()-t))
            print(text)
            if text in str(speak.speakkommand().keys()):
                t = time.time()
                textf = speak.speakkommand()[text][random.randint(0,len(speak.speakkommand()[text])-1)]
                tts.say(textf)
            if time.time()-t>30:
                print(2)
                break