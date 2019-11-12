import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

htmldoc = "https://www.mtggoldfish.com/prices/paper/standard"
page = requests.get(htmldoc)
if page.status_code == 200:
    print("Successful Request")
elif page.status_code == 404:
    print("page not found")
# print(page.text)
#print(page.content)
# tree = html.fromstring(page.content)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())


'''
url = "https://www.cardkingdom.com/mtg/core-set-2020"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
#get the title
title = soup.title
print(title)
#printing text
all_links = soup.find_all('<a>')
print(all_links)
for link in all_links:
    print(link.get('href'))
rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
'''
'''
print(row_td)
print(type(row_td))
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "html.parser").get_text()
print(cleantext)
'''