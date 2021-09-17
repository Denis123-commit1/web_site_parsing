# Леруа Мерлен



# This is the way
# Author: pythontoday
# YouTube: https://www.youtube.com/c/PythonToday/videos

import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import lxml
import json
import csv
import re
from random import choice
from random import uniform
from datetime import datetime
import os

FILE = 'radiators.csv'

# Настраиваем несколько прокси
def get_html(url, useragent = None, proxy = None, params = None):
    print('get_html')
    r = requests.get(url, headers = useragent, proxies = proxy)
    return r.text

def get_pages_count(html):
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find_all("div", class_ = "f11n7m8x_plp")

    if pagination:
        pagination_1 = print(re.search('\d', (pagination[-1].get_text())))
        return int(pagination_1[0])

    else:
        return 1





def get_ip(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "phytpj4_plp")


    radiators = []
    for item in items:
        item_art = re.search('\d{8}', item.text)
        print(item_art)

        if item_art:
            item_art.group(0)
        item_href = 'https://leroymerlin.ru' + item.find_next('a').get('href')
        item_name = re.search(item.text[13:80], item.text)
        item_data = datetime.today().strftime('%Y-%m-%d-%H-%M')
        item_price = re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text)
        # for_adding = all_categories_dict_rad_stal[item_art.group(0)] = item_name.group(0), item_href, item_data, item_price.group(0).replace(" ","")
        radiators.append({
            'link' : item_href,
            'name' : item_name.group(0),
            'date' : item_data,
            'price': item_price.group(0).replace(" ",""),
            'art': item_art.group(0)
        })
    return radiators

def save_json(name):
    with open(f"{name}", "w", encoding='utf8') as file:
        json.dump({name}, file, indent=4, ensure_ascii=False)


def load_json(name):
    with open(f"{name}", encoding="utf8") as file:
        name = json.load(file)


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ссылка', 'имя', 'дата', 'Цена в руб', 'артикул'])
        for item in items:
            writer.writerow([item['link'], item['name'], item['date'], item['price'], item['art']])


def parse():
    url = "https://leroymerlin.ru/catalogue/radiatory-bimetallicheskie/"
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')
    # Создаем видимость что парсит человек и рандомизируем прокси и юзер агент
    for i in range(4):
        sleep(uniform(3, 12))
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}

        html = get_html(url, useragent, proxy)
        radiators = []
        pages_count = int(get_pages_count(html))
        print(pages_count)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(url, params={'page': page})
            radiators.extend(get_ip(html.text))
        save_file(radiators, FILE)
        print(f'Получено {len(radiators)} материалов')
        os.startfile(FILE)



def main():
    parse()




if __name__ == '__main__':
    main()