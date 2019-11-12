from bs4 import BeautifulSoup
import requests

'''
URL Links
Avoid populating this area with anything other than HTML Links
'''
Throne_of_Eldraine_Page = requests.get('https://prices.tcgplayer.com/price-guide/magic/throne-of-eldraine')
'''
End URL links
'''
def ThroneOfEldraine():
    if Throne_of_Eldraine_Page.status_code is not 200:
        raise Exception("Throne of Eldraine TCGPlayer page link not working")
    soup = BeautifulSoup(Throne_of_Eldraine_Page.content, 'html.parser')
    html_list = soup.prettify().splitlines()
    start_marker = 0
    for each in html_list:
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

def __main__():
    ThroneOfEldraine()

if __name__ == "__main__":
    __main__()