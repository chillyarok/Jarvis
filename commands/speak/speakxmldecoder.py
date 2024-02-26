import xml.etree.ElementTree as ET
def speakkommand():
    tree = ET.parse('commands\\speak\\speak.xml')
    root = tree.getroot()
    answers = {}
    for child in root:
        phrase = str(*child.attrib.values())
        ret = []
        for answer in child:
            ret.append(answer.text)
        answers[phrase] = ret
    return answers