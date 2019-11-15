'''
Author: Alex Mensen-Johnson
Init Date: 11/06/20
Push Date: invalid
DNE
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import dovpanda
'''
import relative packages
'''

'''
URL Links
Avoid populating this area with anything other than HTML Links
'''
Throne_of_Eldraine_Page = requests.get('https://prices.tcgplayer.com/price-guide/magic/throne-of-eldraine')
'''
End URL links
'''
soup = BeautifulSoup(Throne_of_Eldraine_Page.content,'html.parser')
a_tags = []
td_tags = []
def unwantedTagRemovalAssnst(tags = []):
    for tag in tags:
        print(tag)
    print(len(tags))

a_tags = soup.find_all('a')
td_tags = soup.find_all('td')

class TOE_Scraper():
    def __init__(self):
        self.trim_a_tags = a_tags[7:len(a_tags)-44]
        self.trim_td_tags = td_tags[:len(td_tags)-7]
        chowder = BeautifulSoup(self.trim_a_tags.__str__(),'html.parser')
        raw_a_text = []
        for line in chowder.get_text().splitlines():
            if "" is not line:
                raw_a_text.append(line[2:-2])
        raw_a_text[-1] += "t"
        chowder = BeautifulSoup(self.trim_td_tags.__str__(),'html.parser')
        raw_td_tags = []
        for line in chowder.get_text().splitlines():
            if "" is not line.strip() and ',' is not line.strip() and 'view' is not line.strip().lower():
                print(line.strip().lower())
'''
Method Throne Of Eldrain Method:
Params: None
Output:None
Version1:
'''
def _ThroneOfEldraine_method1():#Method most likely not used.
    #Conditional Statement: checks websites response
    if Throne_of_Eldraine_Page.status_code is not 200:
        #Terminate Program if unable to access Site
        raise Exception("Throne of Eldraine TCGPlayer page link not working")
    #Beautiful Soup Object:
    soup = BeautifulSoup(Throne_of_Eldraine_Page.content, 'html.parser')
    #html file split into a list of strings
    html_list = soup.prettify().splitlines()
    #starting marker
    start_marker = 0
    #iterataing across lost
    for each in html_list:
        #searches for the html tag <tbody: Note. this can break for two reasons. If another
        if each.__contains__("tbody"):
            break
        start_marker += 1
    print(start_marker)
    print(html_list[start_marker])
    stop_marker = 0
    for each in html_list:
        if each.__contains__("/tbody"):
            break
        stop_marker += 1
    print(stop_marker)
    print(html_list[stop_marker])
    table_list = html_list[start_marker:stop_marker]
    for each in table_list:
        print(each)
'''
Method: Throne Of Eldraine method 2
Params: None
Ouput: None
Version 1
inspiration fr class
'''

_def ThroneOfEldraine_method2():
    #Server Request Success Check
    if Throne_of_Eldraine_Page.status_code is not 200:#Request 200 indicates a succesful request
        raise Exception("Throne of Eldraine TCGPlayer page link not working")
    else:
        print("Successful Request")
    '''
    Class: BeautifulSoup
    Params: html content,parser
    output: Beautiful Soup Object
    '''
    for i in a_tags: print("\'{}\',".format(i))
    tags = soup.find_all('td')
    unprocessed_card_names = []
    unprocessed_values = []
    for tag in tags:
        unprocessed_card_names.append(tag.find_all('a').__str__())
        unprocessed_values.append(tag.__str__())
    '''
    tag handling and removal for values
    '''
    scrubbed_values = []
    for each in unprocessed_values:
        for deeper in each.splitlines():
            if "<" not in deeper:
                scrubbed_values.append(deeper.strip())
    '''
    name extraction
    '''
    scrubbed_names = []
    for each in unprocessed_card_names:
        for split in each.splitlines():
            if len(split) is not 2:
                for split_again in split.split(","):
                    if ''''"<" not in split_again and ''' 'Product Click' not in split_again:
                        # print(split_again.split('\''))
                        for god_help in split_again.split('\''):
                            if '<' not in god_help and '>' not in god_help and god_help is not ''\
                                and 'Price Guide' not in god_help and 'Product Click' not in god_help \
                                    and 'https' not in god_help:
                                scrubbed_names.append(god_help)
    '''
    post scrub ops
    Dictionary building
    '''
    print("{} = {}".format(len(scrubbed_names),len(scrubbed_values)))
    print("last value = --{}--".format(scrubbed_values[-1]))
    columns = ['Name','Rarity','Number','Market Price','Buylist Market Price','Listed Median']
    data_frame = pd.DataFrame(columns=columns)
    data_frame['Name'] = scrubbed_names
    print(data_frame.tail())
    Rarity = []
    Number = []
    Market_Price = []
    Buylist = []
    Median = []
    Rarity_Tokens = ['C','V','R','M','T']
    count = 0
    flag = False
    for scrub in scrubbed_values:
        if scrub in Rarity_Tokens:
            Rarity.append(scrub)
            if scrub == 'T':
                flag = True
        elif count%4 == 0:
            count += 1
            if flag is False:
                Number.append(scrub)
            else:
                flag = False
                Number.append(float('nan'))
        elif count%4 == 1:
            count +=1
            Market_Price.append(scrub)
        elif count%4 == 2:
            count +=1
            Buylist.append(scrub)
        elif count%4 == 3:
            count+=1
            Median.append(scrub)
        else:
            print('unsorted value!! = {}\ntype = {}'.format(each,type(each)))
    print('Rarity = {}\nMarket_Price = {}\nBuylist = {}\nMedian = {}'.format(len(Rarity),len(Market_Price),
                                                                             len(Buylist),len(Median)))
    print(data_frame.size)
    data_frame['Rarity'] = Rarity
    data_frame['Market Price'] = Market_Price
    data_frame['Buylist Market Price'] = Buylist
    data_frame['Listed Median'] = Median


        #if each.__contains__('<'):
         #   unprocessed_values.remove(each)
    #for each in unprocessed_values[0:5]:
        #print(each)
    #print(tags[0])
      #  text.append(found)
    #for each in text:
     #   print(each)

    # table = bs.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "Table1")
    # rows = table.findAll(lambda tag: tag.name == 'tr')
    # print(table)

def __main__():
    #unwantedTagRemovalAssnst(td_tags)
    TOE_Scraper()
    # ThroneOfEldraine_method2()

if __name__ == "__main__":
    __main__()