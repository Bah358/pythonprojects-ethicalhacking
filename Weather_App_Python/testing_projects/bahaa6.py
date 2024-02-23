import math
def primeFactors(n):
    c=2
    while(n>1):
        if(n%c==0):
            print(c,end=" ")
            n=n/c
        else:
            c=c+1
if __name__=="__main__":
    n=input("enter the number")
    primeFactors(n)
    

