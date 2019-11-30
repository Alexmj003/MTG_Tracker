'''
Author: Alex Mensen-Johnson
Init Date: 11/06/20
Push Date: invalid
DNE
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt
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
        self.names, Rarity, Card_Number, Market_Price, BuyList_Price, Listed_Median= [], [], [], [], [], []
        keeper = 0
        for line in chowder.get_text().splitlines():
            temp = line.strip()
            if "" is not temp and ',' is not temp and not temp.__contains__("View"):
                raw_td_tags.append(temp)
        del raw_td_tags[0]
        del raw_td_tags[-1]
        count = 0
        index = 0
        cheat_values = ["C","R","U","M","T","L"]
        Numbers = ['1','2','3','4','5','6','7','8','9','0']
        unique_values = []
        for each in raw_td_tags:
            #print(each + " -> " + str(count))
            # print("{} -> {}".format(each,index))
            # print(each)
            index += 1
            if each.__contains__("$") or each.__contains__("—"):
                if count == 0:
                    Market_Price.append(each)
                     # print("{} added to Market Price\n".format(each))
                elif count == 1:
                    BuyList_Price.append(each)
                     # print("{} added to BuyList Price\n".format(each))
                elif count == 2:
                    Listed_Median.append(each)
                    # print("{} added to Listed Median\n".format(each))
                count += 1
            elif each in cheat_values:
                Rarity.append(each)
                if each == "T":
                    Card_Number.append(float("NaN"))
            elif each[0] in Numbers:
                Card_Number.append(int(each))
            elif each is not "View":
                self.names.append(each)
            if count > 2:
                count = 0 
        '''
        Integer conversion: removal of the dollar sign
        '''

        for i in range(len(self.names)):
            if Market_Price[i] != "—":
                Market_Price[i] = float(Market_Price[i].strip("$"))
            else:
                Market_Price[i] = float("NaN")
            if BuyList_Price[i] != "—":
                BuyList_Price[i] = float(BuyList_Price[i].strip("$"))
            else:
                BuyList_Price[i] = float("NaN")
            if Listed_Median[i] != "—":
                Listed_Median[i] = float(Listed_Median[i].strip("$"))
            else:
                Listed_Median[i] = float("NaN")
        self.Card_Frame = pd.DataFrame(columns=["Name","CardID","Rarity","Market Price","Buy List Price","Listed Median"])
        self.Card_Frame["Name"] = self.names
        # Card_Frame["CardID"] = Card_Number
        self.Card_Frame["Rarity"] = Rarity
        self.Card_Frame["Market Price"] = Market_Price
        self.Card_Frame["Buy List Price"] = BuyList_Price
        self.Card_Frame["Listed Median"] = Listed_Median

    def getFrame(self):
        return self.Card_Frame
        # return Card_Frame

        '''
        count = 0
        while count < len(raw_td_tags):
            Names.append(raw_td_tags[count])
            count +=1
            Rarity.append(raw_td_tags[count])
            print(raw_td_tags[count] + " ->" + str(count))
            if raw_td_tags[count - 1] == "T":
                Card_Number.append(float('NaN'))
                print("Enter the condition")
            else:
                count += 1
                Card_Number.append(raw_td_tags[count])
                count += 1
            if raw_td_tags[count] == "-":
                Market_Price.append(float('NaN'))
            else:
                Market_Price.append(raw_td_tags[count])
            count += 1
            if raw_td_tags[count] == "-":
                BuyList_Price.append(float('NaN'))
            else:
                BuyList_Price.append(raw_td_tags[count])
            count += 1
            if raw_td_tags[count] == "-":
                Listed_Median.append(float('NaN'))
            else:
                Listed_Median.append(raw_td_tags[count])
            count += 2
            print(raw_td_tags[count] + ' -> ' + str(count) )
        Column_names = ['Card Name',Rarity,'Market Price','Buy List Price','Listed Median']
        card_table = pd.DataFrame(columns=Column_names)
        '''
        '''
        for each in raw_td_tags:
            if each.lower() == "view":
                raw_td_tags.remove(each)
        '''


def __main__():
    #unwantedTagRemovalAssnst(td_tags)
    TOE = TOE_Scraper()
    frame = TOE.getFrame()
    #frame.to_json("JSON_FIles/mtgjson/Throne_Of_Eldraine{}.json".format(dt.date.today()))
    frame.to_excel("/Users/idky/PycharmProjects/WebScraping/ExcelFiles/Throne_Of_Eldraine{}.xlsx".format(dt.date.today()))

    # ThroneOfEldraine_method2()

if __name__ == "__main__":
    __main__()