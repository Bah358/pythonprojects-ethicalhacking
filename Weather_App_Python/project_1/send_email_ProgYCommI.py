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

import smtplib      # smtp - Simple Mail Transport Protocol - library for sending email
import time
import sys

# Use the smtp library to send an email
def sendemail( username, password, recipient, subject, msgbody ):
    print (username, password, recipient, subject, msgbody)
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

# Say hello (ehlo) to smtp server, we must follow the protocol !
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
# Provide your login credentials to gain access to server functions
    smtpserver.login(username, password)

# Prepare email header information and message body
    header = 'To: ' +  recipient + '\n' + 'From: ' + username
    header = header + '\n' + 'Subject:' + subject + '\n'
    fullmsg = header + '\n' + msgbody + ' \n\n'

# Show the full message on the screen
    print (fullmsg)

# Send it to the recipient user using the SMTP server
    smtpserver.sendmail(username, recipient, fullmsg)

# Close the connection with the SMTP server
    smtpserver.close()
    print ("Email succesfully sent to recipient !")



if  __name__ == "__main__" :

#  This part where we ask the user the information needed to send
# the email can be improved by getting the information from the command line
# or even getting some of the information from a file. For example, instead
# of getting the message body with input (so only a long single line can be given)
#  you could get the message body reading it from a text file.
#  We get your login and google app password from the file mailsender.txt
    f = open("mailsender.txt","r")
    words = f.read().split()
    username = words[0]
    password = words[1]
    f.close()
    recipient = input("Target email: ")
    subject = input("Subject? ")
    msgbody = input("Message ? ")
    sendemail(username, password, recipient, subject, msgbody )
