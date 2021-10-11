# Леруа Мерлен

# https://hidemy.name/ru/proxy-list/?type=h&anon=4#list (прокси отсюда брал)
# https://spys.one/

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


def get_ip(html):
    print('New proxy & New UserAgent:')
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", class_ = "phytpj4_plp")
    items_1 = soup.find_all("span", class_="cef202m_plp")
    # category = items_1[0].find_next('a', class_="bex6mjh_plp l1ulcka1_plp sztb90a_plp").get('href')
    # category_1 = items_1[1].find_next('a', class_="bex6mjh_plp l1ulcka1_plp sztb90a_plp").get('href')
    # category_2 = items_1[0].find_next("h1", class_="t3y6ha_plp h9z5efi_plp tohqtaw_plp").get_text()
    radiators = []
    for item in items:
        # Взять свой title
        try:
            category = items_1[0].find_next('a', class_="bex6mjh_plp l1ulcka1_plp sztb90a_plp").get('href')
            category_1 = items_1[1].find_next('a', class_="bex6mjh_plp l1ulcka1_plp sztb90a_plp").get('href')
            category_2 = items_1[0].find_next("h1", class_="t3y6ha_plp h9z5efi_plp tohqtaw_plp").get_text()
            radiators.append({
                'link' : 'https://leroymerlin.ru' + item.find_next('a').get('href'),
                'title' : item.find_next("span", class_="t9jup0e_plp p1h8lbu4_plp").get_text(),
                'date' : datetime.today().strftime('%Y-%m-%d-%H-%M'),
                'price' : item.find_next("p", class_="t3y6ha_plp xc1n09g_plp p1q9hgmc_plp").get_text(),
                'art': item.find_next("span", class_="t3y6ha_plp sn92g85_plp p16wqyak_plp").get_text(),
                'catalogue': category,
                'catalogue_1': category_1,
                'catalogue_2': category_2
            })
        except (AttributeError, ConnectionError):
            category = None
            category_1 = None
            category_2 = None
            print('\Имя не найдено')
    return radiators



def save_file(items, path):
    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ссылка', 'имя', 'дата', 'Цена в руб', 'артикул', 'каталог', 'подкаталог_1','подкаталог_2'])
        for item in items:
            writer.writerow([item['link'], item['title'], item['date'], item['price'], item['art'], item['catalogue'], item['catalogue_1'],item['catalogue_2']])


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
    # with open(f"catalog_items.json", "a", encoding="utf-8") as file:
    #     json.dump(catalog_list, file, indent=4, ensure_ascii=False)
    # print('-' * 20)


        # Создаем список с подкатегориями
        # with open(f"catalog_items.json", encoding="utf8") as file:
        #     catalog_items = json.load(file)
        # for k, url_1 in enumerate(catalog_items):
        #     useragents = open('useragents.txt').read().split('\n')
        #     proxies = open('proxies.txt').read().split('\n')
        #     # sleep(uniform(3, 12))
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
        #     # исправить, не выходит из цикла
        #     if k == 16:
        #         break
        #
        #     with open("catalog_items_1.json", "a", encoding="utf-8") as file_1:
        #         json.dump(catalog_items_1, file_1, indent=4, ensure_ascii=False)
        #         print('#'*20)

        #
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

    # Доработать цикл break

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

    # добавляем к списку ссылки на перехода на страницу
    # with open("catalog_items_1_1_1_1.json", encoding="utf8") as file:
    #     catalog_items_1_1_1_1 = json.load(file)
    # catalog_items_1_1_1_1_1 = []
    # for item in catalog_items_1_1_1_1:
    #     item_1 = item + "?page="
    #     catalog_items_1_1_1_1_1.append(item_1)
    #
    # # подумать над дубликатами в парсере, приходится убирать в ручную
    #
    # with open(f"catalog_items_1_1_1_1_1.json", "a", encoding="utf-8") as file:
    #     json.dump(catalog_items_1_1_1_1_1, file, indent=4, ensure_ascii=False)
    # print('-' * 20)

    pass


def parse():
    # Блок кода для создания списков
    # url = f'https://leroymerlin.ru/catalogue/'
    # useragents = open('useragents.txt').read().split('\n')
    # proxies = open('proxies.txt').read().split('\n')
    # Парсится долго, попробовать убрать функцию из цикла и использовать до цикла которую
    # # sleep(uniform(3, 12))
    # for i in range(4):
    #     sleep(uniform(3, 12))
    #     proxy = {'http': 'http://' + choice(proxies)}
    #     useragent = {'User-Agent': choice(useragents)}
    #     html = get_html(url, useragent, proxy)
    #     associated_list(html)


    with open(f"catalog_items_1_1_1_1_1.json", encoding="utf8") as file:
        catalog_items_1_1_1_1_1 = json.load(file)
        # если парсер по каким то причинам прекратит парсить, будет возможность вернуться
        catalog_items_1_1_1_1_2 = catalog_items_1_1_1_1_1[908:]
    for k, url_for_inserting in enumerate(catalog_items_1_1_1_1_2):
        materials = []
        for k_3,page in enumerate(range(1, 600, 1) ):
            print(page)
            url = f'{url_for_inserting}{page}'
            useragents = open('useragents.txt').read().split('\n')
            proxies = open('proxies.txt').read().split('\n')
            sleep(uniform(1, 2))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            try:
                html = get_html(url, useragent, proxy)
                substring = "access blocked"
                print(f"{url}") and quit() if substring in f"{html.lower()}" else print("ok")
                # quit() and print(f"{url}") if f"{html}".find(substring) == 1 else print("ok")
                materials.extend(get_ip(html))
                materials_2 = []
                materials_1 = []
                count = 0
                for i_1 in materials:
                    materials_2.append(i_1)
                    if i_1 not in materials_1:
                        count = count + 1
                        materials_1.append(i_1)
                if len(materials_2) > len(materials_1):  # для проверки ставить здесь брейкпоинт на true false
                    break
                else:
                    continue
            except ConnectionError:
                print("error")
                continue
            # substring = "access blocked"
            # a = quit() and print(f"{url}") if html.lower().find(substring) == 1 else print("ok")

            # if html.lower().index(substring):
            #     break
            # else:
            #     continue

            # materials.extend(get_ip(html))
            # materials_2 = []
            # materials_1 = []
            # count = 0
            # for i_1 in materials:
            #     materials_2.append(i_1)
            #     if i_1 not in materials_1:
            #         count = count + 1
            #         materials_1.append(i_1)
            # if len(materials_2) > len(materials_1): # для проверки ставить здесь брейкпоинт на true false
            #     break
            # else:
            #     continue

        save_file(materials, FILE)
        print(f'Получено {len(materials)} материалов')

    # pass # После получения таблички можно создать функцию переноса по значениям в pandas


# Идеи для дальнейшей работы:
# def carry_over_table(table): # для переноса данных по значению
#     pass

# распараллелить процессы


def main():
    parse()



if __name__ == '__main__':
    main()

