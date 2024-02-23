def loadDictfromFile(fhandle):
    dictfile={}
    currentkey=""
    for x in fhandle:
        entry=x.split(" ",1)
        if (entry.len()==1):
            if(entry[0]!="\n"):
                currentkey=entry[0].rstrip()
                dictfile[currentkey]={}
            else:
                currentkey=""
        else:
                innerdict=dictfile[currentkey]
                innerdict[entry[0]]=entry[1].rstrip()
    return dictfile

f=open("hahaha.txt,r")
dictfile=loadDictfromFile(f)
f.close()
print(dictfile)