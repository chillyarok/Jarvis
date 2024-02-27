import datetime
dayss = {1:"первое",2:"второе",3:"третье",4:"четвёртое",5:"пятое",6:"шестое",7:"седьмое",8:"восьмое",9:"девятое",10:"десятое",11:"одинадцатое",12:"двенадцатое",13:"тренадцатое",14:"четырнадцатое",15:"пятнадцатое",16:"шеснадцатое",17:"семнадцатое",18:"восемнадцатое",19:"девятнадцатое",20:"двадцатое",21:"двадцать первое",22:"двадцать второе",23:"двадцать третье",24:"двадцать четвёртое",25:"двадцать пятое",26:"двадцать шестое",27:"двадцать седьмое",28:"двадцать восьмое",29:"двадцать девятое",30:"тридцатое",31:"тридцать первое"}#дополнить до шестидесяти
monthsandtime = {1:"января",2:"февраля",3:"марта",4:"апреля",5:"мая",6:"июня",7:"июля",8:"августа",9:"сентября",10:"октября",11:"ноября",12:"декабря"}
weekd = {"Mon":"Понедельник","Tue":"Вторник","Wed":"Среда","Thu":"Четверг","Fri":"Пятница","Sat":"Суббота","Sun":"Воскресенье"}
def howdate():
    nowmonth = datetime.datetime.now().month
    nowday = datetime.datetime.now().day
    nowweekday = datetime.datetime.now().ctime().[:3]
    date = f"{dayss[nowday]} {monthsandtime[nowmonth]}. {weekd[nowweekday]}."
    return date

def howtime():
    howhour = str(datetime.datetime.now().time().hour)
    print(howhour)
    time = f"{monthsandtime[howhour]} часов"
howtime()