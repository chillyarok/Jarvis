from xml.etree.ElementTree import parse
import num2words
def xmlr():
    act_phrases = []
    tree = parse('commands\\weather\\act_phrases.xml')
    root = tree.getroot()
    commands = root[0]
    for phrase in commands:
        act_phrases.append(str(phrase.text))
    return act_phrases
def main():
    from requests import get
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+'Krasnodar'+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = get(url).json()
    temperature = round(weather_data['main']['temp'])
    weather = weather_data['weather'][0]['description']
    return f'Сейчас {num2words.num2words(int(temperature),lang="ru")} градусов. {str(weather)}.'
def speak(detected_text:str):  
    act_phrases = xmlr()
    if detected_text in act_phrases:
        return(main())

