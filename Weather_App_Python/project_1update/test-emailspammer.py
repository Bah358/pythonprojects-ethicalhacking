import sys
# We imported the emailspammerlib module
# to be able to make objects (instances) of the
# class emailspammer
# we also imported the sys which is a build in class in python that allows python to create a list of 
# argv that are the data we enter in the command line and that we can call them
# using sys.argv[and the index of the argv we want]
import emailspammerlib

if __name__ == '__main__':
    # Make here an instance of the emailspammer class
    spammer = emailspammerlib.emailspammer()
    # here we followed what was asked for us in the project as to call the functions we created 
    # so we used the instance of the class emailspammer that we created and which is the spammer 
    # in order to execute the functions we created in emailspammer where the arguments of these
    # functions are the data we enter in the command line when executing as they are the 
    # the values inside the list of sys.argv[]
    spammer.loadPersonalInformation(sys.argv[1])
    spammer.loadBodyMessageTemplate(sys.argv[2])
    spammer.sendPersonalizedEmails()
    
    # Use the arguments in sys.argv[] to use the emailspammer
    # object as we ask in documentation of the project for
    # the test program:
