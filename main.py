import requests
from bs4 import BeautifulSoup
from enviaM import envia
import pandas as pd


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83'}

def getReq(url):    
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')
    return soup

        
def parse(htmlElement):
    productList = []
    products = htmlElement.findAll('div',class_='productCard')
    for item in products:
        price = (item.find('span',class_='priceCard').text.replace('R$\xa0','').replace('.','').replace(',','.'))
        if '---' in price:
            return
        price = float(price)
        if price <= 1000.00:
            product = {
                'price':(price),
                'name':item.find('span',class_='nameCard').text.replace('â' and 'Â','a'),
                'link': 'https://www.kabum.com.br' + item.find('a')['href'],
            }
            productList.append(product)
    return productList 
         

def output(list):
    prodcutsDF = pd.DataFrame(list)
    prodcutsDF.to_csv('output.csv',index = False)
    return


def main():
    site = 'https://www.kabum.com.br/computadores/monitores?page_number=1&page_size=100&facet_filters=&sort=most_searched'
    soup = getReq(site)
    products = parse(soup)
    output(products)
    return 0

main()