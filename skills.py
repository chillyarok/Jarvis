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
    if "хром" in text:
        engine.say("открываю")
        time.sleep(2)
        subprocess.run(["C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"])
    elif "браузер" in text:
        engine.say("открываю")
        time.sleep(2)
        subprocess.run(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
    else:
        engine.say("такое приложение не найдено")
    return text
