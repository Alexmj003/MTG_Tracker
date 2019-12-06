import pandas as pd
import os
practice_file = "/Users/idky/PycharmProjects/WebScraping/ExcelFiles/Throne_Of_Eldraine2019-11-23.xlsx"
practice_path = "/Users/idky/PycharmProjects/WebScraping/ExcelFiles"
def piper(table = practice_file):
    df = pd.read_excel(table)
    splitlip = table.split(('/'))
    target_values = splitlip[-1]
    target_values = target_values[:-5]
    date = target_values[-10:]
    target_values = target_values[:-10]
    target_values = target_values.strip('_')
    another_list = target_values.split('_')
    set_name = ""
    print(date)
    for each in another_list:
        set_name += (each + " ")
    set_name = set_name[:-1]
    for index, row in df.iterrows():
        Card_Name = row['Name']
        Card_Name = Card_Name.replace("'","").replace(',','')
        print(Card_Name)
        Rarity = row['Rarity']
        Market_Price = row['Market Price']
        Buy_List = row['Buy List Price']
        Listed_Median = row['Listed Median']
        #insert method here


def do_the_loop(path = practice_path):
    listerman = os.listdir(path)
    for each in listerman:
        if each.__contains__('.xlsx'):
            piper("{}/{}".format(path,each))

do_the_loop()