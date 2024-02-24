import json,pyaudio
from vosk import Model, KaldiRecognizer
import pyttsx3
import skills
import func
import xml.etree.ElementTree as ET
'''xml'''
answer = dict()
tree = ET.parse("commands\speak\speak.xml")
root = tree.getroot()
for child in root:
    ph = child.attrib.get('phrase')
    an = child[0].text.split()
    answer[ph]=an

start_phrases = func.table_to_list("start phrases.txt")
engine = pyttsx3.init()
engine.setProperty('rate',120)
engine.setProperty("volune",1.0)
'''vosk'''
model = Model('models\\vosk-model-small-ru-0.22')
rec = KaldiRecognizer(model, 16000)
paudio = pyaudio.PyAudio()
stream = paudio.open(format=pyaudio.paInt16, channels=1,rate=16000,input=True,frames_per_buffer=8000)
stream.start_stream()
print("good")
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
            if text in answer.keys():
                engine.say(answer[text][0])
                engine.runAndWait()
            if text=="пока":
                break
            if "открой" in text:
                print(skills.open_prog(text))
            engine.runAndWait()
            if "расскажи анекдот" in text:
                skills.say_anegdot(text)

    
