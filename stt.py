import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model("models\\vosk-model-small-ru-0.22")
sample_rate = 16000
device_id = 1
q = queue.Queue()
def callback(indata,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    q.put(bytes(indata))
def listen():
    with sd.RawInputStream(samplerate=sample_rate,blocksize=8000,device=device_id,dtype="int16",channels=1,callback=callback):
        rec = vosk.KaldiRecognizer(model,sample_rate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
                yield rec.Result