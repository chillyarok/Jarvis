import json,pyaudio
from vosk import Model, KaldiRecognizer
import pyttsx3
import skills
import func
phrases = func.table_to_list("phrases.txt")
answers = func.table_to_list("answers.txt")
start_phrases = func.table_to_list("start phrases.txt")
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty("volune",1.0)
model = Model('D:\kortana\\model_s')
rec = KaldiRecognizer(model, 16000)
paudio = pyaudio.PyAudio()
stream = paudio.open(format=pyaudio.paInt16, channels=1,rate=16000,input=True,frames_per_buffer=8000)
stream.start_stream()
def speech_to_text():
    while True:
        data = stream.read(4000,exception_on_overflow=False)
        if rec.AcceptWaveform(data) and (len(data))>0:
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]
for text in speech_to_text():
    print(text)
    if text in start_phrases:
        for text in speech_to_text():
            print(text)
            if text in phrases:
                engine.say(answers[phrases.index(text)])
            if text=="пока":
                break
            if "открой" in text:
                print(skills.open_prog(text))
            engine.runAndWait()

    engine.runAndWait()
