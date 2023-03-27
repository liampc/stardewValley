import requests
from bs4 import BeautifulSoup
import csv
import re


page = requests.get("https://stardewvalleywiki.com/Crops")
soup = BeautifulSoup(page.text, 'html.parser')


# data = soup.find_all('span', attrs={'class','mw-headline'})
# data_list = []

# count = 1
# for crop in crops:
#     d = {}
#     d['Crop Number'] = f'Crop {count}'
#     d['Crop Name'] = crop.text
#     count += 1
#     crops_list.append(d)




# filename = 'products.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['Crop Number', 'Crop Name'])
#     w.writeheader()

#     w.writerows(crops_list)




# crops = soup.select('table.no-wrap > tbody > tr > td:nth-child(2)')
# crops_list = []

# count = 1
# for crop in crops:
#     d = {}
#     d['Crop Number'] = f'Crop {count}'
#     d['Crop Name'] = crop.text.strip()
#     count += 1
#     crops_list.append(d)


# filename = 'products.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['Crop Number', 'Crop Name'])
#     w.writeheader()

#     w.writerows(crops_list)



def findPrice():
    for child in soup.find_all('td', text = re.compile('[0-9]{2,6}g')):
        print(child.getText())

def findHealth():
    for child in soup.find_all('td', style='vertical-align: bottom;'):
        print(child.getText())


def findSeller():
    divs = soup.find_all('div', style='text-align: left; padding-top: 1.5em;')

    for child in divs:
        links = child.find_all('a')
        for link in links:
            if len(links) < 2:
                print(link.getText())
                print('null')
            else:
                print(link.getText())


def findSellerPrice():
    divs = soup.find_all('div', style='text-align: left; padding-top: 1.5em;')

    for child in divs:
        links = child.find_all('span', {'class': 'no-wrap'})
        for link in links:
            if len(links) < 2:
                print(link.getText())
                print('null')
            else:
                print(link.getText())


findSellerPrice()