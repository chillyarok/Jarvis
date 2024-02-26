import xml.etree.ElementTree as ET
def speakkommand():
    tree = ET.parse('commands\\speak\\speak.xml')
    root = tree.getroot()
    frases = {}
    answers = []
    for child in root:
        phrase = str(*child.attrib.values())
        for answer in child:
            answers.append(answer.text)
    frases[phrase] = answers
    return frases
