def loadPersonalinformation(fname):
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
        
        

