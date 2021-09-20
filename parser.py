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
from itertools import groupby

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


        #
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

        with open('catalog_items_1.json') as f:
            data = json.loads("[" +
                              f.read().replace("\n}{", "\n},{") +
                              "]")
        # print(data)
        result = {}
        for d in data:
            result.update(d)
        # print(result)
        valuesList = list(result.values())


        def unique(obj: iter):
            args = []
            for a in obj:
                if a not in args:
                    args.append(a)
                    yield a


        new_valuesList = unique(valuesList)
        # new_valuesList = [el for el, _ in groupby(valuesList)]
        with open(f"catalog_items_1_1.json", "a", encoding="utf-8") as file:
            json.dump([*new_valuesList], file, indent=4, ensure_ascii=False)
        print('-' * 20)

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

    # with open('catalog_items_1.json') as f:
    #     data = json.loads("[" +
    #                       f.read().replace("\n}{", "\n},{") +
    #                       "]")
    # # print(data)
    # result = {}
    # for d in data:
    #     result.update(d)
    # # print(result)
    # valuesList = list(result.values())
    # # print(valuesList)
    # with open(f"catalog_items_1_1.json", "a", encoding="utf-8") as file:
    #     json.dump(valuesList, file, indent=4, ensure_ascii=False)
    # print('-' * 20)







# with open(f'catalog_items_6.json') as f:
    #     catalog_items_6 = json.loads(f.readline(delimiter = "\n"))

    # with open("catalog_items_5.json", encoding="utf8") as file:
    #     catalog_items_5 = json.loads(file)
    # res = sum(catalog_items_5, [])
    # for url_2 in res:
    #     useragents = open('useragents.txt').read().split('\n')
    #     proxies = open('proxies.txt').read().split('\n')
    #
    #     sleep(uniform(3, 12))
    #     proxy = {'http': 'http://' + choice(proxies)}
    #     useragent = {'User-Agent': choice(useragents)}
    #     req_1 = get_html(url_2, useragent, proxy)
    #     # req = requests.get(url = url_1)
    #     print('Next_parser_2')
    #     soup_2 = BeautifulSoup(req_1, 'lxml')
    #     info_block_1 = soup_2.find_all("a", {"class":"bex6mjh_plp", "data-qa":"catalog-link"})
    #     catalog_items_2 = []
    #     for item_2 in info_block_1:
    #         item_link_2 = 'https://leroymerlin.ru' + item_2.get('href')
    #         catalog_items_2 += item_link_2
    #     with open(f"catalog_items_4.json", "a", encoding="utf-8") as file_2:
    #         json.dump(catalog_items_2, file_2, indent=4, ensure_ascii=False)
    #     print('&' * 20)


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

def listmerge2(catalog):
    all = []
    for lst in catalog:
        all = all + lst
    with open(f"catalog_items_5.json", "a", encoding="utf-8") as file_2:
        json.dump(all, file_2, indent=4, ensure_ascii=False)
    print('&' * 20)


def main():
    parse()




if __name__ == '__main__':
    main()




# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst_1 = [[1,1], [2,2], [3,3]]
# res = sum(lst, [])
# print(res)
# for i in lst:
#     for i_1 in lst_1:
#         print()
# from itertools import groupby
# lst = [[1,2,3],[1,4,5],[2,6,7]]
# new_lst = list(set(sum(lst, [])))
# # new_x = [el for el, _ in groupby(lst)]
# print(new_lst)


# st = list(set(['1', '2', '3', '4', '5']))
# print(st[4])


# lst = [1, 2]
# lst_1 = [3,4]
# lst_2 = lst + lst_1
# print(lst_2)

# dic = {'s' : 1}
# print(dic.keys())

# dict_list = [{'a': 1, 'b': 2}, {'a': 3}]
# result = {}
# for d in dict_list:
#   result.update(d)
#
# print(result)

# x = [1,2,3,4,5,1,2,3]
# def unique(obj: iter):
#     args = []
#     for a in obj:
#         if a not in args:
#             args.append(a)
#             yield a
#
# r = unique(x)
# print(r)
# print('original sort unique:', [*r])