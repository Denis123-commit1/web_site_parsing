import requests
from bs4 import BeautifulSoup

# Переменные как константы пишем в верхнем регистре
URL = 'https://auto.ria.com/car/used/'
HEADERS = {'user-agent': 'Chrome/93.0.4577.63', 'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r







def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_ = 'ticket-item') # Если здесь указать то, что выше "a.proposition",
    # то нет никаких проблем с выводом ссылки



    cars = []
    for item in items:
        usd_price = item.find('div', class_='price-ticket')
        if usd_price:
            usd_price = usd_price.get_text().replace('\xa0', '')
            usd_price = usd_price.replace('•', ', ')
        else:
            usd_price = 'Цену уточняйте'


        cars.append({
            'title': item.find('span', class_='blue bold').get_text(strip=True),
            'link': item.find('a',class_ = 'm-link-ticket').get('href'),
            # 'usd_price': item.find('div', class_='price-ticket').get_text(),
            # 'uah_price': item.find('span', class_='size16').get_text(),
            'usd_price': usd_price
            # 'city': item.find('span', class_='item region').get_text(),
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

