# We need to import your module send_email_ProgYCommI
# to be able to make an instance of the class SendMail

from bahaa15 import send
import send_email_ProgYCommI

#
# In this python module you define
# your class emailspammer with the member
# functions we ask in the requirements
# of the project. Here you will find
# the headers of the mandatory member functions,
# that you need to implement.
# But of course, you can define any other member
# functions you need to use

class emailspammer():
    """docstring explaining what this class
    is.
    """

# You can pass to the init function any mandatory
# arguments you need when making an object of
# this class
    def __init__(self):
        # One mandatory action, you will need an object
        # of your  class SendMail
        self.smail =  send_email_ProgYCommI.SendMail('smtp.gmail.com', 587)
        

    def loadpersonalinformation(self, fname):
        fname=open('email.txt')
        counter=1
        d={}
        mylist=[]
        for line in fname:
            if ("counter=1"):
                d["email"]=line
            if ("counter=2"):
                d["greetings"]=line
            if ("counter=3"):
                d["name"]=line
            if ("counter=4"):
                d["surname"]=line
            if ("counter=5"):
                d["end"]=line
                mylist.append(d)
                d={}
                counter=0
            counter+=1
        return mylist

    def resetPersonalInformation(self):
        mylist=self.loadpersonalinformation()
        mylist.clear()
        return mylist

    def loadbodymessagetemplate(self,tempbodymsgfile):
        mylist=self.loadpersonalinformation()
        tempbodymsgfile=open('tempbodymsgfile.txt')
        mylist2=[]
        i=0
        j=0
        mylist3=[]
        while(j<=len(mylist)):
            dterms={mylist[j]}
            for line in tempbodymsgfile:
                mylist2[i]=mylist2.append(line)
                while(i<len(mylist2)):
                    for key in dterms:
                        mylist2[i]=mylist2[i].replace(key,dterms(key))
                i+=1
            mylist3[j]=mylist3.append(mylist2)
            j+=1
            mylist2=[]
            i=0
        return mylist3
        
    def sendPersonalizedEmails( self ):
        f = open("mailsender.txt","r")
        words = f.read().split()
        username = words[0]
        password = words[1]
        f.close()
        sendmessage=send()
        username=input("Enter Username")
        password=input("Enter Password")
        i=0
        mylist=self.loadpersonalinformation()
        msgbody=self.loadbodymessagetemplate()
        for x in mylist:
            dterms={mylist[i]}
            recipient = dterms('email')
            subject= ("Merry Christmas")
            sendmessage.sendemail(username, password, recipient, subject, msgbody[i] )
            i+=1
            


        

        


