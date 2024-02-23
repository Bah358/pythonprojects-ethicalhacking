def div(a,b):
    if(a<b):
        a=input("enter the new number")
        div(a,b)
    else:
        r=a%b
        q=a/b
        print(r,q)
if __name__=="__main__":        
    a=input("enter the first number")
    b=input("enter the second number")
    div(int (a), int (b))
    
