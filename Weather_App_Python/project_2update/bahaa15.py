#!/bin/env python3
#
# Beware, you must now use  google App password authentication to send email trhough
# google smtp servers. Look here:
#
#
# https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317
#
#
# EXERCISE:
#
#  Encapsulate the following function into a class object, SendMail, that performs
#  the work of sending an email in four phases, each one implemented in a different
#  method (member function) of the SendMail object class. There will be four
#  member functions:
#
#  1) In the __init__ function we simply collect and save the values for the
#  variables: SMTP_SERVER, SMTP_PORT.
#  and then create the SMTP server object and send to it the initial SMTP messages.
#  Observe that the SMTP  server object must be saved as a member variable
#  of the class instance (so with the self.variablename syntax)
#
#  2) In the   function login(username, password) we perform the login operation to
#     the SMTP server
#
#  3) In the function sendemail(recipient,subject,msgbody) we will prepare and send the
#      email with msgbody "the text of the message" to the user with address recipient
#       Observe that this function will need the value of the variable username
#       (that will be the sending (from) user of the email). So, this information should
#       be stored INSIDE the SendMail object when calling the previous function (login)
#
#  4) In the function close() we will close the connection with the SMTP server
#
# So, the function you have below does all the work in sequence, but you have to
# separate the code of this function in the four substeps (phases) mentioned above.

# in this class we are going to do different functions in order to send and email



import smtplib      # smtp - Simple Mail Transport Protocol - library for sending email
import time
import sys
class send():
        # so we are going tp start with init function that on initialization of this class
        # it open the port "587" responsible for sending files and requests the server that 
        # is the SMPTP server
   
        def __init__(self):
                self.SMPTP_SERVER="smtp.gmail.com"
                self.SMTP_PORT= 587
        # in this function called login we are going to login to the gmail that we are going to send from 
        # it the messages so in order to login to it there is a methadology called sync/ack which is the
        # synchronize and acknowledge that will take place between our device and the smtp server using the 
        # the ehlo and starttls functions that are found in python library and using them we can attain 
        # this methadolgy and then we use the login with the username and password of our account in order 
        # to login        
        def login(self,username,password):
                self.smtpserver = smtplib.SMTP( self.SMPTP_SERVER,self.SMTP_PORT)
                self.smtpserver.ehlo()
                self.smtpserver.starttls()
                self.smtpserver.ehlo()
                self.smtpserver.login(username, password)
                self.username=username
                self.password=password
        

# Use the smtp library to send an email
        # here we are going to do another function called sendemail in which we use the arguments related to
        # the recipient of the message and the subject of the message and the actual message
        # and we print this these details to make sure that we sending the coreect message to the correct
        #  recipient
        def sendemail(self,recipient, subject, msgbody ):
        
                print (recipient, subject, msgbody)
        


       

                # Prepare email header information and message body
                # so we are prparing the email header we include the recipeint,subject and fullmsg
                header = 'To: ' +  recipient + '\n' + 'From: ' + self.username
                header = header + '\n' + 'Subject:' + subject + '\n'
                fullmsg = header + '\n' + msgbody + ' \n\n'

                # Show the full message on the screen
                # by using theis print function and then we use the sendmail function found in python library
                #  and we do it on the smptpserver having the arguments of username of our account the recipeint
                #  and the fullmsg
                print (fullmsg)
                self.smtpserver.sendmail(self.username, recipient, fullmsg)

# Send it to the recipient user using the SMTP server
        
        # Close the connection with the SMTP server
        # using this function that we created called closeconnection and that uses the function in
        # python library that closes the connection and the we print that the email sent successfully
        def closeconnection(self):
                self.smtpserver.close()
                print ("Email succesfully sent to recipient !")



