import subprocess
import pyttsx3
import time
import func
ways = func.table_to_list("prog_ways.txt")
progs = func.table_to_list("prog_phrases.txt")
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty("volune",1.0)
def open_prog(text):
    text = text.split()
    text = " ".join(text[1:])
    for i in progs:
        if i in text or text in i:
            engine.say("открываю.")
            engine.runAndWait()
            time.sleep(0.5)
            subprocess.run(ways[progs.index(i)])
            