i=0 
value=input("insert your elements seperated by space")
print("\n")
list=value.split()
print ("list:", list)
for x in list:
    while(i<len(list)):
        if(x<list[i]):
            print("(", x ,",", list[i] ,")" )
            print("\n")
            i+=1
        else:
            i+=1
    i=0    
            

        

    

