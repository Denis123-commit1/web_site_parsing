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
        # pagination_1 = print(re.search('\d', (pagination[-1].get_text())))
        pagination_1 = re.search('\d', pagination[-1].get_text()).group(0)
        return pagination_1
    else:
        return 1





def get_ip(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "phytpj4_plp")


    radiators = []
    for item in items:
        # item_art = re.search('\d{8}', item.text)
        # print(item_art)
        #
        # if item_art:
        #     item_art.group(0)
        # item_href = 'https://leroymerlin.ru' + item.find_next('a').get('href')
        # item_name = re.search(item.text[13:80], item.text)
        # item_data = datetime.today().strftime('%Y-%m-%d-%H-%M')
        # item_price = re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text)
        # for_adding = all_categories_dict_rad_stal[item_art.group(0)] = item_name.group(0), item_href, item_data, item_price.group(0).replace(" ","")
        radiators.append({
            'link' : 'https://leroymerlin.ru' + item.find_next('a').get('href'),
            'name' : re.search(item.text[13:80], item.text).group(0),
            'date' : datetime.today().strftime('%Y-%m-%d-%H-%M'),
            'price': re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text).group(0).replace(" ",""),
            'art': re.search('\d{8}', item.text).group(0)
        })
    return radiators
    # with open("radiatoryyyyyy.json", "w", encoding='utf8') as file:
    #     json.dump(radiators, file, indent=4, ensure_ascii=False)
    # print('---'*20)
    # save_json(radiators)

def save_json(name):
    with open(f"{name}.json", "w", encoding='utf8') as file:
        json.dump(f"{name}.json", file, indent=4, ensure_ascii=False)


def load_json(name):
    with open(f"{name}", encoding="utf8") as file:
        name = json.load(file)


def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ссылка', 'имя', 'дата', 'Цена в руб', 'артикул'])
        for item in items:
            writer.writerow([item['link'], item['name'], item['date'], item['price'], item['art']])


def associated_list(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "title")
    catalog_list = []
    for item in items:
        item_name = item.text.replace("\n", "")
        catalog_list.append(item_name)
        for
    with open(f"catalog_items.json", "a", encoding="utf-8") as file:
        json.dump(catalog_list, file, indent=4, ensure_ascii=False)
    print('-'*20)


def parse():

    url = f'https://leroymerlin.ru/catalogue/'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')
    # pages_count = get_pages_count(html)
    # html = get_html(url)
    # html = get_html(url, useragent, proxy, params={'page': page})

    for i in range(4):
        sleep(uniform(3, 12))
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        radiators = []
        # pages_count = get_pages_count(html)
        html = get_html(url, useragent, proxy)
        associated_list(html)
        # pages_count = get_pages_count(html)
        # for page in range(1, int(pages_count) + 1):
        #     print(f'Парсинг страницы {page} из {pages_count}...')
        #     # html = get_html(url, useragent, proxy, params={'page': page})
        #     radiators.extend(get_ip(html))
        # save_file(radiators, FILE)
        # print(f'Получено {len(radiators)} материалов')



def main():
    parse()




if __name__ == '__main__':
    main()