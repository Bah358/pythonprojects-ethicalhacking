import weattherinfolib # here we iported the program weattherinfolib in order to use its class



# here and in the program that we are going to execute we first created an object called test1 which is an 
# object of the class weatherinfo that is found in the program that we imported and which is weattherinfolib
# then we used the functions that we have in the class weatherinfo which is the loadLocations that we passed to 
# it the argument info_file which has the data that this function is going to load as we specified before
# then we used the sendWeatherInfo function that is going to send the message to the recipeints as specified 
#also before

if __name__ == "__main__":

    test1=weattherinfolib.weatherinfo()

    test1.loadLocations("info_file")

    test1.sendWeatherInfo()