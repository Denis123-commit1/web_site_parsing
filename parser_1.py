import requests
from bs4 import BeautifulSoup
import csv
import os

# Переменные как константы пишем в верхнем регистре
URL = 'https://auto.ria.com/car/used/'
HEADERS = {'user-agent': 'Chrome/93.0.4577.63', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    # pagination = soup.find_all('span', class_='page-item mhide')

    pagination = soup.find_all('span', class_='page-item mhide', \
                               limit=2)
    print(pagination)
    # if pagination:
    #     return int(pagination[-1].get_text())
    # else:
    #     return 1





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
    return cars

# def save_file(items, path):
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['Марка', 'Ссылка', 'Цена в $'])
#         for item in items:
#             writer.writerow([item['title'], item['link'], item['usd_price']])


def parse():
    # URL = input('Введите URL: ')
    # URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        # cars = []
        pages_count = get_pages_count(html.text)
        # for page in range(1, pages_count + 1):
        #     print(f'Парсинг страницы {page} из {pages_count}...')
        #     html = get_html(URL, params={'page': page})
        #     cars.extend(get_content(html.text))
        # save_file(cars, FILE)
        # print(f'Получено {len(cars)} автомобилей')
        # os.startfile(FILE)
    else:
        print('Error')


parse()

