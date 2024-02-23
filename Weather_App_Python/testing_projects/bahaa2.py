def getInput():
    velocity,time=input("enter velocity and time")
def vpos(t,vy,g=9.8):
    left=vy*t
    right=0.5*vy*pow(t,2)
    subtract=left-right
    return subtract

if __name__ == "__main__":
    velocity, time = getInput()
    result=vpos(time,velocity)
    if (result<=0):
        print("jjdjsjsj")
    else:
        print(result)

   
