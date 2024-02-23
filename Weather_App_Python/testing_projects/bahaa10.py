def replaceTemplateLine(line,dterms):
    for key in dterms:
        line=line.replace(key,dterms[key])
    return line

if __name__=="__main__":
    line=input("give me list of lines")
    d={"Name":"Bahaa","Sur":"Yehia"}
    res=replaceTemplateLine(line,d)
    print(res)


            
        