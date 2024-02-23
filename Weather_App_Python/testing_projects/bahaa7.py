def gcdExtended(a,b):
    if(a==0):
        return b,0,1
    
    gcd,x1,y1=gcdExtended(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    i=i+1
    return gcd,x,y,i

if __name__=="__main__":
    a=input("please enter the number")
    b=input('please enter the second number')
    g,x,y,i=gcdExtended(a,b)
    print("gcd of",a,"and",b,"is",g,"and the coefficients are",x,y,"and number of iteration is",i,)

    