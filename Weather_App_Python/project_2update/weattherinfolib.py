import bahaa15 # we imported this in order to use the send email class and use its functions in our class here

import requests

import sys

import json

# here we are implementing the class weatherinfo that is goint to load data from a file having the email
# of the recipeint that we are going to send the message to and the location of this place and lattitude
# and longitude of this place

class weatherinfo():
    # in this init function we made this class upon initialization to create and object of the class send
    # found in "bahaa15" and we also prepared an empty list as a data stucture that we are going to put the 
    # data in
    def __init__(self):

        self.smail = bahaa15.send()

        self.info_list = []


    # in this function we openned the info file that has our data and we prepared an empty dictionary
    # where we are going to put the data inside and then put every dictionary inside the list that we 
    # have previously initialized and thus to have a list of dictionaries so in every line in our info_file
    # we first split the line between spaces using the split function and thus we will have an array 
    # called line1 that has every string we splitted of this line and then we assigned a keyword for the  
    # dictionary with the coressponding data of it where this data we get by calling the array line1 with 
    # coressponding index and then append this dictionary that we created to the empty list"info_list" that 
    # we have initialized before and thus we have our first dictionary in our list and then we empty our 
    # dictionary and we go again with the same process but with the second line of the info_file using the loop
    # and we repeat this same process untill all the lines in info_file ends 
    def loadLocations(self, info_file):

        data = open(info_file)

        d = {}



        for line in data:

            line1 = line.split()

            d["email"] = line1[0]

            d["location"] = line1[1]

            d["lattitude"] = line1[2]

            d["longitude"] = line1[3]

            self.info_list.append(d)

            d = {}



    # here in this function we are going to send the weather info

    def sendWeatherInfo(self):

        # self.url = "http://api.openweathermap.org/data/2.5/forecast?cnt=8&units=metric&mode=json&"

        # so we used this url that is a request to the openweathermap as the domain and to the folders
        # cnt assigning it to 8 which gives us 8 different timings where the difference between these different 
        # timings will be 3 hours and the units in metric and the mode which is the type of the data 
        # will be in json format


        self.url = "http://api.openweathermap.org/data/2.5/forecast?cnt=8&units=metric&mode=json"



        # here we start using one function of the object smail of the class send that we have initialized 
        # in order to login to our account and we pass the arguments of our username and password of our 
        #account

        self.smail.login("yehiabahaa3@gmail.com", "hhytpzudtqrlpolh")

        # here we go through every index of our info_list which in other words we are going through every 
        # dictionary info of our info_list and then using the keywords of this dictionary we assign 
        # the data of the recipeint and the subject. Then we add to the url that we had the latitude and the
        # the longitude by also using the keyword of our dictionary info that coressponds to the lattitude 
        # and longitude. We also use the sys.argv that we used by importing the sys in our class in order
        # to add to the url also the appid but we used this way so that when we are executing the program in 
        # the shell we can add the appid which can be different than ours and thus this appid will be 
        # added to the url in order to perform the request and we gave sys.argv the index 1 because our command
        # in the shell will be sys.argv of index 0 and then come the appid which will be of index 1  

        for info in self.info_list:

            self.recipient = info["email"]

            self.subject = info["location"]

            self.url = self.url + "&lat=" + info["lattitude"] + "&lon=" + info["longitude"] + "&appid=" + sys.argv[1]

            # here we are getting the response by using the get function and passing the completed url to it
            # then we take this response that is in json and we apply the loads function that transforms
            # it to python dictionary called as jsondict

            self.response = requests.get(self.url)

            self.jsondict =  json.loads(self.response.text)

            # here we assigned message_to_send to be empty and then we go through every timeslot in our
            # dictionary jsondict with the keyword that we know it is called list from the data presented
            # in the openweather site and then for every time slot we assignned a msg_body that we used 
            # a structure called f''' which is a formatted string that we can format the string as we
            # like so we can have a better view og the data and to avoid string concatenation and we 
            # then get the data that we want each with its corresponding keyword inside our dictionary
            # tslot which is another dictionary in the jsondict dictionary of keyword list and after
            # getting the information we then add these information t0 message_to_send and it will be the first
            # time slot then we make \n to go on another line and we go for the second time slot using the 
            # loop we are looping through tslots in the jsondict with the keyword list every time and 
            # we do the same process for the seconf time slot untill all 8 time slots are finieshed 
            # the we will have the message_to_send ready to be sent to the recipeint with all the data 
            # presented in a good view in it 

            self.message_to_send = ""

            for tslot in self.jsondict['list']:

                

                self.msgbody = f'''

                -> at: {tslot[ "dt_txt"]}

                -> min t: {tslot["main"]["temp_min"]}

                -> max t: {tslot["main"]["temp_max"]}

                -> wind speed: {tslot["wind"]["speed"]}

                -> wind deg: {tslot["wind"]["deg"]}

                -> wind gust: {tslot["wind"]["gust"]}

                -> pop: {tslot["pop"]}

                '''



            

                self.message_to_send = f'{self.message_to_send}\n{self.msgbody}'

            # then here after everything is ready we use the function sendemail from the smail of the class
            # send in order to send the nessage and here this will be outside the loop of tslot but inside
            # the loop of info of our info_list in order to send the message message_to_send all with all the
            # data of the 8 time slots to this reciepeint one time 



            

            self.smail.sendemail( self.recipient, self.subject, self.message_to_send)
        # here we close the connection and that is after we finish sending to all recipeints in order to open 
        # the connection one time and do what we want to do and then close one time and this is the advantage
        # of using the object smail of the class send in our class in this program here
        self.smail.closeconnection()

