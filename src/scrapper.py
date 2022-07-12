# # #!/usr/bin/python
# # # -*- coding: ascii -*-
import json
import bs4
import requests


def getAgent(filename, target):
    with open(filename) as f:
        data = json.load(f)
        token = data[target]
        return token


def find_price(ticker):
    headers = getAgent('agent.json', 'agent')
    # headers = {
    #     'OR ADD HEADER HERE'
    # }

    url = 'https://finance.yahoo.com/quote/%s/' % ticker
    response = requests.get(url, headers=headers)
    print()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].text

    # print(price[:price.find('T')] + 'T')
    return price[:price.find('T')] + 'T'


def get_price(price):
    return price[:price.find('-')]


def get_change(price):
    return price[price.find('-'):price.find('(')]


def get_percent_change(price):
    return price[price.find('('):price.find(')')] + ')'


def get_just_quote(price):
    return price[:price.find('A')]

# if __name__ == '__main__':
#     for i in range(2):
#         find_price('SPY')
#         find_price('QQQ')
#         find_price('IWM')
#         time_wait = 1
#         print(f'Waiting {time_wait} seconds...')
#         time.sleep(time_wait)
