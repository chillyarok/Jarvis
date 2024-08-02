from xml.etree.ElementTree import parse
from core.tts import say
def xmlr():
    act_phrases = []
    tree = parse('commands\\example new module\\act_phrases.xml') # example new module меняется на папку с вашим модулем
    root = tree.getroot()
    commands = root[0]
    for phrase in commands:
        act_phrases.append(str(phrase.text))
    return act_phrases
def main():
    '''логика вашего модуля'''

    return()#то что нужно вывести
def speak(detected_text:str):  
    act_phrases = xmlr()
    if detected_text in act_phrases:
        pass
        #say(main())


