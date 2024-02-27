import datetime
import dicts_for_whattime as dicts
def howdate():
    nowmonth = datetime.datetime.now().month
    nowday = datetime.datetime.now().day
    nowweekday = datetime.datetime.now().ctime()[:3]
    date = f"{dicts.dayss[nowday]} {dicts.months[nowmonth]}. {dicts.weekd[nowweekday]}."
    return date

def howtime():
    howhour = str(datetime.datetime.now().time().hour)
    howmin = str(datetime.datetime.now().minute)
    return f'сейсас, {dicts.times[howhour]} {dicts.times[howmin]}'
howtime()