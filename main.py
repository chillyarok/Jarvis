import tts
import stt
import commands.xmldecoder as speak
import wake_word_detect as wwd
import random



print("good")
while True:
    if wwd.WakeWordDetect() == True:
        print(1)
        for text in stt.listen():
            print(text)
            if text in str(speak.speakkommand().keys()):
                textf = speak.speakkommand()[text][random.randint(0,len(speak.speakkommand()[text])-1)]
                tts.say(textf)