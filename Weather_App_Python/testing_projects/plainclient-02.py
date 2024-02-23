import requests
import sys
import json

# Examples of very simple web pages (no javascript code or other stuff):
# 
#  https://www.york.ac.uk/teaching/cws/wws/webpage1.html
#  http://www.columbia.edu/~fdc/sample.htmls
# Execute this program passing as its unique argument the URL of the web page to
# download:
#
#   python3 ./plaintclient-02.py  https://www.york.ac.uk/teaching/cws/wws/webpage1.html

# connect to a web server and get a response object 
# to interact with the server and get the contents
# of the URL requested
responsehandle  = requests.get( sys.argv[1] )

# read the lines of the HTML file requested in the URL
# iterating through the lines of the document

# This next is for getting the webpage, line per line
#for line in responsehandle:
#  line = line.decode('UTF-8').rstrip()
#  print (line)
  
# This next if you want to read the whole webpage in a single string:

wholewebtext = responsehandle.text
print(wholewebtext)


