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
    items = soup.find_all('a', class_='proposition_link')

    # print(items)

    cars = []
    for item in items:
        # uah_price = item.find('span', class_='size15')
        # if uah_price:
        #     uah_price = uah_price.get_text().replace(' • ', '')
        # else:
        #     uah_price = 'Цену уточняйте'
        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': item.find('span', class_='link').get('a href'),
            # 'usd_price': item.find('strong', class_='green').get_text(),
            # 'uah_price': uah_price,
            # 'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text(),
        })
    print(cars) # Проверка количества названий автомобилей
    # print(len(cars))
    # return cars

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
