import bahaa15

if  __name__ == "__main__" :

#  This part where we ask the user the information needed to send
# the email can be improved by getting the information from the command line
# or even getting some of the information from a file. For example, instead
# of getting the message body with input (so only a long single line can be given)
#  you could get the message body reading it from a text file.
#  We get your login and google app password from the file mailsender.txt
    
    username ="yehiabahaa3@gmail.com"
    password = "hhytpzudtqrlpolh"
    recipient = input("Target email: ")
    subject = input("Subject? ")
    msgbody = input("Message ? ")
    spammer=bahaa15.send()
    spammer.login(username,password)
    spammer.sendemail(recipient,subject,msgbody)
    spammer.closeconnection()
    