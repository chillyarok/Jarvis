import tts
import stt
import commands.speak.speakxmldecoder
import wake_word_detect as wwd




print("start")
while True:
    if wwd.WakeWordDetect() == True:
        print(1)
        while True:
            print(25)