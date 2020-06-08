# Intellimide_internship_WebScrapping

# Introduction

This is a solution to the problem given to me for the IntelliMind internship

It contains two files.
 - Run.sh
 - web_scrapper.py
 
1)Run.sh

This is a Shell script file.It runs the python script.

2)web_scrapper.py

This is the main solution.I have used 'Selenium' and 'BeautifulSoap' module to acheive webscrapping.
I studied the url given and found out the common element in the data to be scrapped,here being the attr called 'data-ng-bind' as 'cell'.
Then,i used the selenium to access the web page and beautiful soap to parse it.
and lastly,i got the data from soap and converted it into a json format and outputted the data into terminal
