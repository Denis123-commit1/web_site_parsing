import requests
from bs4 import BeautifulSoup

# Переменные как константы пишем в верхнем регистре
URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Chrome/93.0.4577.63', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r







def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_ = 'proposition_link') # Если здесь указать то, что выше "a.proposition",
    # то нет никаких проблем с выводом ссылки



    cars = []
    for item in items:


        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            # 'link': HOST + item.find('a',class_ = 'proposition_link').get('href'),
            'usd_price': item.find('span', class_='green').get_text(),
            'uah_price': item.find('span', class_='size16').get_text(),
            'city': item.find('span', class_='item region').get_text(),
        })
    print(cars)
    return cars




def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # print(html.text) # Выйдет html запрос, который надо будет распарсить
        cars = get_content(html.text)
    else:
        print('Error')


parse()

