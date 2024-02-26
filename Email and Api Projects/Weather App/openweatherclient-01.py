# Example of getting JSON data from openweathermap.org using the
# HTTP request library:  https://requests.readthedocs.io/en/latest/user/quickstart/
#
# Info about the forecast of 5 days request to openweather:
#
#  https://openweathermap.org/forecast5
import requests as reqs
import sys
import json

# connect to a web server and get a response object
# to interact with the server and get the contents
# of the URL requested
# Here we only ask the forecast for the next 8 (3-hours) slots, so cnt=8
# The first argument must be YOUR valid APP Key obtained from the openweathermap service
# when creating your free openweathermap account:
#
#   https://openweathermap.org/appid#apikey
lat=sys.argv[2]
lon=sys.argv[3]
key=sys.argv[1]
url = "https://api.openweathermap.org/data/2.5/forecast?cnt=8&units=metric&mode=json&"
url = url + "lat="+lat+"&lon="+lon+"&appid="+key
response = reqs.get( url )



# Decode the answer text (that will be a json string) as a corresponding
# python dictionaty
# The list of weather forecast for consecutive time slots of three hours will be available in the entry with key 'list'
#
jsondict =  json.loads(response.text)
print(json.dumps(jsondict, indent=4))

# show info only about min/max temperatures of each time slot:
for tslot in jsondict['list']:
   print (tslot[ "dt_txt"], " -> ", "min t: ",tslot['main']['temp_min'] , "max t: ", tslot['main']['temp_max']  )
