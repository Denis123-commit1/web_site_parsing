import requests
from bs4 import BeautifulSoup

# Переменные как константы пишем в верхнем регистре
URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'OPR/78.0.4093.184', 'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='result-explore')

    # print(items)

    cars = []
    for item in items:


        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': item.find('a',class_ = 'proposition_link').get('href'),
            'usd_price': item.find('span', class_='green').get_text(),
            'uah_price': item.find('span', class_='size16').get_text(),
            'city': item.find('span', class_='item region').get_text(),
        })
    print(cars)
    return cars



def parse():
    html = get_html(URL)
    print(html.status_code)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # print(html.text) # Выйдет html запрос, который надо будет распарсить
        cars = get_content(html.text)
    else:
        print('Error')


parse()

