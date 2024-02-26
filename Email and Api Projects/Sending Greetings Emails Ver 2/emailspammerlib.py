# Project Done By Randa Al Othman and Bahaa Yehia
# We need to import the module send_email_ProgYCommI
# to be able to make an instance of the class SendMail
import send_email_ProgYCommI 

#
# In this python module we define
# the class emailspammer with the member
# functions of the project that are teh init function
# the loadPersonalInformation function,the resetPersonalInformation function
# the loadBodyMessageTemplate and the sendPersonalizedEmails function


class emailspammer():
    """docstring explaining what this class
    is.
    """

# You can pass to the init function any mandatory
# arguments you need when making an object of
# this class
    def __init__(self):
        # we need an object of the class SendMail so we defined this object
        # and we defined also an object for the info_list where we are going to load the 
        # Personal Information
        self.smail =  send_email_ProgYCommI.sendemail
        self.info_list = []

    # this function takes to arguments one is self because it is related to the class emailspammer
    # and the other is the info_file were it goes to this file given in order to get the information
    # and load them in the info_list as list of dictionaries d 
    def loadPersonalInformation(self, info_file):
        data = open(info_file)
        counter = 1
        d = {}
        for line in data:
            
            if counter == 1: 
                d["email"] = line
            if counter == 2:
                d["greetings"] = line
            if counter == 3:
                d["name"] = line
            if counter == 4:
                d["surname"] = line
            if counter == 5:
                d["end"] = line
                self.info_list.append(d)
                d = {}
                counter = 0
            counter += 1
        
        
    # this function takes one argument that is self because it is related to the calss emailspammer 
    # and it only clear the info_list as to clear the information

    def resetPersonalInformation( self ):

        self.info_list.clear()

    # this function takes two arguments one which is self similar to the ones before and the 
    # the second argument is the tempbdymsgfile that it opens in order to read it and puts it
    # in the body_text. 
    def loadBodyMessageTemplate(self, tempbodymsgfile):
        
        data = open(tempbodymsgfile)
        body_text = data.read()
        data.close()

        self.body_text=body_text

    # this function takes one argument which is self because it is related to the class emailspammer
    # and what it does is followed up through the steps of this function
    def sendPersonalizedEmails( self ):
        f = open("mailsender.txt","r")
        words = f.read().split()
        username = words[0]
        password = words[1]
        f.close()

       
        # 1. info_list might be already filled so will check it first
        if len(self.info_list) == 0:
            self.loadPersonalInformation('email.txt')


        # 2. get the template body
        template_body = self.body_text

        # loop through the list to send mails
        for info_dict in self.info_list:
            # first modify the body
            modified_body = template_body
            modified_body=modified_body.replace('{INITGREETINGS}', info_dict["greetings"])
            modified_body=modified_body.replace('{NAME}', info_dict["name"])
            modified_body=modified_body.replace('{SURNAME}', info_dict["surname"])
            modified_body=modified_body.replace('{CLOSINGSENTENCE}', info_dict["end"])

            # now we have the body modified and ready to use
            # here we shall call the method send mail
            self.smail(
                username=username,
                password=password,
                recipient=info_dict["email"],
                subject="Merry Christmas\n",
                msgbody=modified_body,
            )












