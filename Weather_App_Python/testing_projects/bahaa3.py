def add(n):
    if n:
        return n + add(n-1)
    else:
        return 0
if __name__=="__main__":
    a=input("enter your number")
    c= add(int(a))
    print(c)
