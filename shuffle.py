import json
import random
import datetime

constellation = [["牡羊座", "Aries"], ["牡牛座", "Taurus"], ["双子座", "Gemini"], ["蟹座", "Cancer"], ["獅子座", "Leo"], ["乙女座", "Virgo"], ["天秤座", "Libra"], ["蠍座", "Scorpio"], ["射手座", "Sagittarius"], ["山羊座", "Capricorn"], ["水瓶座", "Aquarius"], ["魚座", "Pisces"]]
luckyItem = ["傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘", "傘"]
dict = {}

random.shuffle(constellation)
dict["constellation"] = constellation
dict["luckyItem"] = luckyItem

dt_now = datetime.datetime.now()
filename = str(dt_now.date()) + ".json"
fson = open(filename, 'w')
json.dump(dict, fson)
fson.close()
