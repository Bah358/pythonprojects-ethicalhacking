def gcd(a,b):
    if a==0:
        return b
    i=i+1
    return gcd(b%a,a)
i=0
a=input("enter the first number")
b=input("enter the second number")
d=gcd(a,b)
print(d,i)
