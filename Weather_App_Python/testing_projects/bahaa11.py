
def replaceTemplateLine(mylist,dterms):
    mylist2=[]
    i=0
    while(i<len(mylist)):
        for key in dterms:
            mylist[i]=mylist[i].replace(key,dterms[key])
            mylist2.append(mylist[i])
            i+=1
    return mylist2

if __name__=="__main__":
    line1=input("give me list of lines")
    line2=input("give me second line")
    mylist=[line1,line2]
    d={"Name":"Bahaa","surname":"Yehia"}
    mylist2=replaceTemplateLine(mylist,d)
    for j in mylist2:
        print(j)
        

        