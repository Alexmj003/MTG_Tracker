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
    print("succesfull request")
else:
    print("request unsuccesfull")
    raise Exception("Unsuccsefull request")
soup = BeautifulSoup(page.content,'html.parser')
# print(type(soup.prettify()))
html_list = soup.get_text().splitlines()
# print(len(html_list))
start_index = 0
stop_index = 0
for line in html_list:
    if line.lower().__contains__("Mythic".lower()):
        print("start found")
        break
    start_index += 1
for line in html_list:
    if line.lower().__contains__("last updated".lower()):
        print("end found")
        break
    stop_index +=1
text_list = html_list[start_index:stop_index]
filter_list = []
skip = ""
for each in text_list:
    if each == skip:
        skip = skip
    else:
        filter_list.append(each)
# print(len(filter_list))
for each in filter_list:
    print(each)

# print(start_index,stop_index)
# print(soup.get_text())