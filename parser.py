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

def get_pages_count(html):
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find_all("a", {"class": "bex6mjh_plp", "data-qa-pagination-active":"false"})
    if pagination:
        pagination_1 = []
        for item in pagination:
        # pagination_1 = print(re.search('\d', (pagination[-1].get_text())))
            item_obj = int(re.search("\d+", item.get('href')).group(0))
            pagination_1.append(item_obj)
        return pagination_1[-1] + 10
    else:
        return 1 + 10
    # pagination = soup.find_all("div", class_ = "f11n7m8x_plp")
    # pagination_2 = []
    # if pagination:
    #     for item in pagination:
    #         item_obj = int(re.search('\d+', item[-1].get_text()).group(0))
    #         pagination_2.append(item_obj)
    # if pagination:
    #     # pagination_1 = print(re.search((pagination[-1].get_text())))
    #     pagination_1 = int(re.search('\d|\d+', pagination[-1].get("href")).group(0))
    #     return pagination_2
    # else:
    #     return 1





def get_ip(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "phytpj4_plp")
    radiators = []
    for item in items:
        item_price = re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text)
        item_art = re.search('\d{8}', item.text)
        # print(item.text)
        try:
            radiators.append({
                'link' : 'https://leroymerlin.ru' + item.find_next('a').get('href'),
                'name' : re.search(re.search(item.text[item_art.end():item_price.start()], item.text).group(0), item.text).group(0),
                'date' : datetime.today().strftime('%Y-%m-%d-%H-%M'),
                'price': re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text).group(0).replace(" ",""),
                'art': re.search('\d{8}', item.text).group(0)
            })
        except AttributeError:
            print('Имя не найдено')
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
    for k, url_for_inserting in enumerate(catalog_items_1_1_1_1_1):
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
#
# lst = [
#     'a',
#     'b'
# ]
# lst_1 = []
# for i in lst:
#     obj = i + 'a'
#     lst_1.append(obj)
# print(lst_1)