import datetime


times = {
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
dayss = {1:"первое",2:"второе",3:"третье",4:"четвёртое",5:"пятое",6:"шестое",7:"седьмое",8:"восьмое",9:"девятое",10:"десятое",11:"одинадцатое",12:"двенадцатое",13:"тренадцатое",14:"четырнадцатое",15:"пятнадцатое",16:"шеснадцатое",17:"семнадцатое",18:"восемнадцатое",19:"девятнадцатое",20:"двадцатое",21:"двадцать первое",22:"двадцать второе",23:"двадцать третье",24:"двадцать четвёртое",25:"двадцать пятое",26:"двадцать шестое",27:"двадцать седьмое",28:"двадцать восьмое",29:"двадцать девятое",30:"тридцатое",31:"тридцать первое"}
months = {1:"января",2:"февраля",3:"марта",4:"апреля",5:"мая",6:"июня",7:"июля",8:"августа",9:"сентября",10:"октября",11:"ноября",12:"декабря"}
weekd = {"Mon":"Понедельник","Tue":"Вторник","Wed":"Среда","Thu":"Четверг","Fri":"Пятница","Sat":"Суббота","Sun":"Воскресенье"}


def howdate():
    nowmonth = datetime.datetime.now().month
    nowday = datetime.datetime.now().day
    nowweekday = datetime.datetime.now().ctime()[:3]
    date = f"{dayss[nowday]} {months[nowmonth]}. {weekd[nowweekday]}."
    return date

def howtime():
    howhour = str(datetime.datetime.now().time().hour)
    howmin = str(datetime.datetime.now().minute)
    return f'сейсас, {times[howhour]} {times[howmin]} минут'