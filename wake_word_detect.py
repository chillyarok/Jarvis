import pvporcupine
from pvrecorder import PvRecorder
access_key= "PkFORWS+ELPnVKmh+oSdWz57LEFP5+/8TRn+kUAWwTpHRbK14uJoWw=="
porcupine = pvporcupine.create(access_key=access_key, keywords=['jarvis'])
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

def WakeWordDetect():
    try:
        recoder.start()


        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                return True



    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()