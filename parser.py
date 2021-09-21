# Леруа Мерлен



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
from itertools import groupby

FILE = 'materials.csv'

# Настраиваем несколько прокси
def get_html(url, useragent = None, proxy = None, params = None):
    print('get_html')
    r = requests.get(url, headers = useragent, proxies = proxy)
    return r.text

def replace(line, old_new_num):
    # при итерации по списку распаковываем кортежи на
    # старое и новое значения, а так же `n` - количество замен
    for vals in old_new_num:
        # если кортежа имеет 3 элемента,
        # значит присутствует количество замен
        if len(vals) == 3:
            # распаковываем кортеж
            old, new, n = vals
            # передаем аргументы методу и
            line = line.replace(old, new, n)
        elif len(vals) == 2:
            # распаковываем кортеж
            old, new = vals
            line = line.replace(old, new)
        else:
            # если в кортеже НЕ 2 или 3 элемента,
            # то поднимаем исключение
            raise ('кортеж должен состоять из 2-х или 3-х элементов')
    return line

def get_ip(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "phytpj4_plp")
    radiators = []
    for item in items:
        item_price = re.search('\d+\s₽/шт', item.text)
        item_art = re.search('\d{8}', item.text)
        replace_val = [('(', '\('), (')', '\)')]
        # item_name = re.search(item.text[item_art.end():item_price.start()], item.text)
        # item_name_1 = item_name.group(0)
        # item_name_2 = f"{replace(item_name_1, replace_val)}"
        try:
            # item_name_1 = replace(item_name, replace_val)
            radiators.append({
                'link' : 'https://leroymerlin.ru' + item.find_next('a').get('href'),
                'name' : (re.search(item.text[item_art.end():item_price.start()].replace(")", "").replace("(", ""), item.text).group(0)),
                'date' : datetime.today().strftime('%Y-%m-%d-%H-%M'),
                'price': item_price.group(0).replace(" ",""),
                'art': re.search('\d{8}', item.text).group(0)
            })
        except AttributeError:
            print('\Имя не найдено')
    return radiators



def save_file(items, path):
    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ссылка', 'имя', 'дата', 'Цена в руб', 'артикул'])
        for item in items:
            writer.writerow([item['link'], item['name'], item['date'], item['price'], item['art']])

# функция для создания списков (уже создали)
def associated_list(html = None):
    # Создаем список с категориями
    # print('New proxy & New UserAgent:')
    # soup = BeautifulSoup(html, 'lxml')
    # items = soup.find_all("div", class_ = "title")
    # catalog_list = []
    # for item in items:
    #     item_link = "https://leroymerlin.ru" + item.find_next('a').get('href')
    #     catalog_list.append(item_link)
    # # with open(f"catalog_items.json.json", "a", encoding="utf-8") as file:
    # #     json.dump(catalog_list, file, indent=4, ensure_ascii=False)
    # # print('-' * 20)


        # Создаем список с подкатегориями
        # with open(f"catalog_items.json", encoding="utf8") as file:
        #     catalog_items = json.load(file)
        # for k, url_1 in enumerate(catalog_items):
        #     useragents = open('useragents.txt').read().split('\n')
        #     proxies = open('proxies.txt').read().split('\n')
        #     sleep(uniform(3, 12))
        #     proxy = {'http': 'http://' + choice(proxies)}
        #     useragent = {'User-Agent': choice(useragents)}
        #     req = get_html(url_1, useragent, proxy)
        #     print('Next_parser_1')
        #     soup_1 = BeautifulSoup(req, 'lxml')
        #     info_block = soup_1.find_all('a', {"class":"bex6mjh_plp", "data-qa":"catalog-link"})
        #     catalog_items_1 = {}
        #     for i,item_1 in enumerate(info_block):
        #         item_link_1 = 'https://leroymerlin.ru' + item_1.get('href')
        #         catalog_items_1[f"{k, i}"] = item_link_1
        #         if k == 15:
        #             break
        #     with open("catalog_items_1.json", "a", encoding="utf-8") as file_1:
        #         json.dump(catalog_items_1, file_1, indent=4, ensure_ascii=False)
        #         print('#'*20)

        # with open('catalog_items_1.json') as f:
        #     data = json.loads("[" +
        #                       f.read().replace("\n}{", "\n},{") +
        #                       "]")
        # print(data)
        # result = {}
        # for d in data:
        #     result.update(d)
        # print(result)
        # valuesList = list(result.values())
        # def unique(obj: iter):
        #     args = []
        #     for a in obj:
        #         if a not in args:
        #             args.append(a)
        #             yield a
        # new_valuesList = unique(valuesList)
        # with open(f"catalog_items_1_1.json", "a", encoding="utf-8") as file:
        #     json.dump([*new_valuesList], file, indent=4, ensure_ascii=False)
        # print('-' * 20)

    # Создаем список с подкатегориями подкатегорий
    # with open("catalog_items_1_1.json", encoding="utf8") as file:
    #     catalog_items_1_1 = json.load(file)
    # for k_1, url_2 in enumerate(catalog_items_1_1):
    #     useragents = open('useragents.txt').read().split('\n')
    #     proxies = open('proxies.txt').read().split('\n')
    #     sleep(uniform(3, 12))
    #     proxy = {'http': 'http://' + choice(proxies)}
    #     useragent = {'User-Agent': choice(useragents)}
    #     req_1 = get_html(url_2, useragent, proxy)
    #     print('Next_parser_2')
    #     soup_2 = BeautifulSoup(req_1, 'lxml')
    #     info_block_1 = soup_2.find_all("a", {"class":"bex6mjh_plp", "data-qa":"catalog-link"})
    #     catalog_items_1_1_1 = {}
    #     for i_1,item_2 in enumerate(info_block_1):
    #         item_link_1 = 'https://leroymerlin.ru' + item_2.get('href')
    #         catalog_items_1_1_1[f"{k_1, i_1}"] = item_link_1
    #         if k_1 == len(catalog_items_1_1):
    #             break
    #     with open("catalog_items_1_1_1.json", "a", encoding="utf-8") as file_1:
    #         json.dump(catalog_items_1_1_1, file_1, indent=4, ensure_ascii=False)
    #         print('&'*20)

    # with open('catalog_items_1_1_1.json') as f:
    #     data_1 = json.loads("[" +
    #                       f.read().replace("\n}{", "\n},{") +
    #                       "]")
    # # print(data)
    # result_1 = {}
    # for d_1 in data_1:
    #     result_1.update(d_1)
    # # print(result_1)
    # valuesList_1 = list(result_1.values())
    # def unique(obj: iter):
    #     args = []
    #     for a in obj:
    #         if a not in args:
    #             args.append(a)
    #             yield a
    # new_valuesList_1 = unique(valuesList_1)
    # with open(f"catalog_items_1_1_1_1.json", "a", encoding="utf-8") as file:
    #     json.dump([*new_valuesList_1], file, indent=4, ensure_ascii=False)
    # print('-' * 20)


    # with open("catalog_items_1_1_1_1.json", encoding="utf8") as file:
    #     catalog_items_1_1_1_1 = json.load(file)
    # catalog_items_1_1_1_1_1 = []
    # for item in catalog_items_1_1_1_1:
    #     item_1 = item + "?page="
    #     catalog_items_1_1_1_1_1.append(item_1)
    # with open(f"catalog_items_1_1_1_1_1.json", "a", encoding="utf-8") as file:
    #     json.dump(catalog_items_1_1_1_1_1, file, indent=4, ensure_ascii=False)
    # print('-' * 20)

    pass


def parse():

    with open(f"catalog_items_1_1_1_1_1.json", encoding="utf8") as file:
        catalog_items_1_1_1_1_1 = json.load(file)
        catalog_items_1_1_1_1_2 = catalog_items_1_1_1_1_1[17:]
    for k, url_for_inserting in enumerate(catalog_items_1_1_1_1_2):
        materials = []
        for k_3 ,page in enumerate(range(1, 20, 1)):
        # with open(f"catalog_items_1_1_1_1_1.json", encoding="utf8") as file:
        #     catalog_items_1_1_1_1_1 = json.load(file)
        # for k, url_for_inserting in enumerate(catalog_items_1_1_1_1_1):
            print(page)
            url = f'{url_for_inserting}{page}'
            url_last = f'{url_for_inserting}{page -1}'
            url_future = f'{url_for_inserting}{page + 1}'
            useragents = open('useragents.txt').read().split('\n')
            proxies = open('proxies.txt').read().split('\n')
            sleep(uniform(3, 12))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            # materials = []
            html = get_html(url, useragent, proxy)
            sleep(uniform(3, 12))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            html_1 = get_html(url_last, useragent, proxy)
            sleep(uniform(3, 12))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            html_2 = get_html(url_future, useragent, proxy)
            sleep(uniform(3, 12))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            html = get_html(url, useragent, proxy)
            materials.extend(get_ip(html))
            sleep(uniform(3, 12))
            a = [get_ip(html_2)]
            b = [get_ip(html_1)]
            if a == b: # для проверки ставить здесь брейкпоинт на true false
                break
            else:
                continue
        save_file(materials, FILE)
        print(f'Получено {len(materials)} материалов')

    # pass # После получения списка можно создать функцию переноса по значениям в pandas


# def carry_over_table(table): # для переноса данных по значению
#     pass


def main():
    parse()




if __name__ == '__main__':
    main()

# lst = ['a', 'b', 'c']
# lst[1:]

# lst = '12345) ('
# print(lst.replace(")", "").replace("(", ""))