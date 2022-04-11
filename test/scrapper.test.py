import json
import bs4
import requests
import time
from bs4 import BeautifulSoup

def getUserAgent():
    with open('agent.json') as f:
        data = json.load(f)
        user_agent = data["AGENT"]
        return user_agent

def find_price():
    headers = getUserAgent()

    ticker = 'NQ=F'
    # url = (f'https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch')
    url = 'https://finance.yahoo.com/quote/SPY/'
    response = requests.get(url, headers=headers)
    print()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].text
    print(price)
    return price

if __name__ == '__main__':
    while True:
        find_price()
        time_wait = 1
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)
