
chisla = {
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    '10': 'десять',
    '11': 'одиннадцать',
    '12': 'двенадцать',
    '13': 'тринадцать',
    '14': 'четырнадцать',
    '15': 'пятнадцать',
    '16': 'шестнадцать',
    '17': 'семнадцать',
    '18': 'восемнадцать',
    '19': 'девятнадцать',
    '20': 'двадцать',
    '21': 'двадцать один',
    '22': 'двадцать два',
    '23': 'двадцать три',
    '24': 'двадцать четыре',
    '25': 'двадцать пять',
    '26': 'двадцать шесть',
    '27': 'двадцать семь',
    '28': 'двадцать восемь',
    '29': 'двадцать девять',
    '30': 'тридцать',
    '31': 'тридцать один',
    '32': 'тридцать два',
    '33': 'тридцать три',
    '34': 'тридцать четыре',
    '35': 'тридцать пять',
    '36': 'тридцать шесть',
    '37': 'тридцать семь',
    '38': 'тридцать восемь',
    '39': 'тридцать девять',
    '40': 'сорок',
    '50': 'пятьдесят',
    '60': 'шестьдесят'
}

def weatherdecoder():
    f = []
    import xml.etree.ElementTree as ET
    tree = ET.parse('commands\\weather\\weather_info.xml')
    root = tree.getroot()
    ff = root[1]
    for i in ff:
        f.append(i.text)
    print(f)
    return(f)
weatherdecoder()
def howweather():
    import xml.etree.ElementTree as ET
    def weatherinfodecoder():
        tree = ET.parse('commands\\weather\\weather_info.xml')
        root = tree.getroot()
        return root[0].text

    import requests

    url = 'https://api.openweathermap.org/data/2.5/weather?q='+weatherinfodecoder()+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    weather = weather_data['weather'][0]['description']
    return(f'Сейчас {chisla[str(temperature)]} градусов. {str(weather)}.')