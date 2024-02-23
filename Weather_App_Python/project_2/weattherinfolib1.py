import bahaa15
import requests
import json
import sys

class weatherinfo():
    def __init__(self):
        self.smail=bahaa15.send()
        self.info_list=[]
    
    def loadLocations(self, info_file):
        data = open(info_file)
        d = {}
        for line in data:
            line1 = line.split()
            d["email"]=line1[0]
            d["location"]=line1[1]
            d["lattitude"]=line1[2]
            d["longitude"]=line1[3]
            self.info_list.append(d)
            d= {}
            
            
    def sendWeatherInfo(self):
        self.url = "https://api.openweathermap.org/data/2.5/forecast?cnt=8&units=metric&mode=json&"
        self.url = self.url + "appid=" +sys.argv[1]
        self.smail.login(self,"yehiabahaa3@gmail.com","hhytpzudtqrlpolh")
        for info in self.info_list:
            self.recipient=info["email"]
            self.subject=info["location"]
            self.url=self.url + "lat=" +info["lattitude"] + "&lon=" +info["lomgitude"]
            self.response = requests.get(self.url)
            self.jsondict =  json.loads(self.response.text)
            for tslot in self.jsondict['list']:
                self.msgbody= tslot[ "dt_txt"] + " -> " + "min t: " + tslot['main']['temp_min'] + "max t: " + tslot['main']['temp_max'] + tslot['wind'] + tslot['pop']
                self.smail.sendemail(self,self.recipient,self.subject,self.msgbody)
        self.smail.closeconnection()    