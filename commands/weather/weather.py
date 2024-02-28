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
    return(f'Сейчас {str(temperature)} градусов. {weather}.')