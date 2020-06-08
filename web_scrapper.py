#importing all dependencies
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import sys
#it loads the webpage in a BeautifulSoup object
def loadWebpage_In_Soup(url):
    
    #path of chromedriver..may change according to another pc
    path = r'C:/chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(url)
    return BeautifulSoup(driver.page_source,'html.parser')
	
	

#it finds all the tags with the given names which has the attr mentioned in dict of attr
def get_allTag(tag,dict_Of_Attr,soup):
    
    return soup.find_all(tag,dict_Of_Attr)
	
	

# this function does the web scrapping and return a json response of symbol and names in the given url
def web_scrapping_symbols_names(url):
    
    #url to scrap is given as parameter
    soup = loadWebpage_In_Soup(url)
    
    #we get all <a> tags with data-ng-bind attr
    symbols_html = get_allTag('a',{'data-ng-bind':'cell'},soup)
    
    #retrieves the text of all <a> tag
    symbols = [symbol.text for symbol in symbols_html]
    
    #we get all span tag with data-ng-bind attr
    names_html = get_allTag('span',{'data-ng-bind':'cell'},soup)
    names =[]
    
    #we take the text of every ninth span element as they are the names
    for idx,name in enumerate(names_html):
        if(idx % 9 == 0 ):
            names.append(name.text)
    result = []
    
    #creates a list combining the two list of symbols and names
    for i in range(len(names)):
        result.append({'Symbol':symbols[i],'Name':names[i]})
        
    #returns the json of the result list
    return json.dumps(result)

	
#calling the main function
url = 'https://www.barchart.com/stocks/quotes/GOOG/competitors'
print(web_scrapping_symbols_names(url))