import json
import random
import datetime

constellation = [["牡羊座", "Aries"], ["牡牛座", "Taurus"], ["双子座", "Gemini"], ["蟹座", "Cancer"], ["獅子座", "Leo"], ["乙女座", "Virgo"], ["天秤座", "Libra"], ["蠍座", "Scorpio"], ["射手座", "Sagittarius"], ["山羊座", "Capricorn"], ["水瓶座", "Aquarius"], ["魚座", "Pisces"]]
luckyItem = ["傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘"]
filename = "TodayLucks.json"

def copyArchive():
    fson = open(filename, 'r')
    copyDiction = json.loads(fson.read())
    fson.close()
    year = copyDiction["year"]
    month = copyDiction["month"]
    day = copyDiction["day"]
    stryear = str(year)
    if (month < 10):
        strmonth = "0" + str(month)
    else:
        strmonth = str(month)
    if (day < 10):
        strday = "0" + str(day)
    else:
        strday = str(day)
    copyFilename = "archives/" + stryear + "-" + strmonth + "-" + strday + ".json"
    copyFson = open(copyFilename, 'w')
    json.dump(copyDiction, copyFson)
    copyFson.close()

def generateTodayLucks():
    diction = {}
    dt_today = datetime.datetime.today()
    random.shuffle(constellation)
    diction["constellation"] = constellation
    diction["luckyItem"] = luckyItem
    diction["year"] = dt_today.year
    diction["month"] = dt_today.month
    diction["day"] = dt_today.day
    fson = open(filename, 'w')
    json.dump(diction, fson)
    fson.close()

copyArchive()
generateTodayLucks()




