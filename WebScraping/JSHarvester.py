import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import sys
sys.path
sys.path.append('/Users/idky/PycharmProjects/WebScraping/phantomjs-2.1.1-macosx')
print(sys.path)

'''
Targeting MTG Stocks entry Acclaimed Contender
'''
target_url = "https://www.mtgstocks.com/prints/50228"
driver = webdriver.PhantomJS()
driver.get(target_url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
print('here')
driver.quit()