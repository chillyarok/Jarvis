import vosk
import json
import pyaudio

model = vosk.Model("core\\vosk-model-small-ru-0.22")
sample_rate = 16000
rec = vosk.KaldiRecognizer(model, sample_rate)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=sample_rate,input=True,frames_per_buffer=8000)
stream.start_stream()
def listen():
    while True:
        data = stream.read(4000,exception_on_overflow=False)
        if rec.AcceptWaveform(data) and len(data)>0:
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer['text']