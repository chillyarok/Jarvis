import tts
import stt
import commands.speak.speakxmldecoder
import wake_word_detect as wwd




print("good")
while True:
    if wwd.WakeWordDetect() == True:
        print(1)
        while True:
            print(stt.listen())