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




# Настраиваем несколько прокси
def get_html(url, useragent = None, proxy = None):
    print('get_html')
    r = requests.get(url, headers = useragent, proxies = proxy)
    return r.text

def get_pages_count(html):
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.find_all("div", class_ = "f11n7m8x_plp")
    if pagination:
        return int(float(pagination[-1].get_text()))
    else:
        return 1





def get_ip(html):
    soup = BeautifulSoup(html, "lxml")
    all_products_hrefs = soup.find_all("a", {"class":"bex6mjh_plp", "data-qa":"catalog-link"})

    all_categories_dict_for_radiators_and_elther = {}
    for item in all_products_hrefs:
        item_text = item.text
        item_href_1 = 'https://leroymerlin.ru/' + item.get("href")
        # print(item_href_1)
        all_categories_dict_for_radiators_and_elther[item_text] = item_href_1

    # with open("all_categories_dict_for_radiators_and_elther.json", "w", encoding='utf8') as file:
    #     json.dump(all_categories_dict_for_radiators_and_elther, file, indent=4, ensure_ascii=False)
    # print('---'*20)

    iteration_count = int(len(all_categories_dict_for_radiators_and_elther)) - 1
    count = 0
    print(f"Всего итераций: {iteration_count}")


    # for item_href_1 in all_categories_dict_for_radiators_and_elther:
    #
    #     print('New proxy & New UserAgent:')
    #     soup = BeautifulSoup(item_href_1, 'lxml')
    #     all_products_hrefs = soup.find_all("div", class_ = "phytpj4_plp")
    #     all_categories_dict_rad_stal = {}
    #     for item in all_products_hrefs:
    #         item_art = re.search('\d{8}', item.text)
    #         if item_art:
    #             item_art.group(0)
    #         item_href = 'https://leroymerlin.ru' + item.find_next('a').get('href')
    #         item_name = re.search(item.text[13:80], item.text)
    #         item_data = datetime.now()
    #         item_price = re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text)
    #         for_adding = all_categories_dict_rad_stal[item_art.group(0)] = item_name.group(0), item_href, item_data, item_price.group(0).replace(" ","")
    #
    #         with open(f"data/{item_text}.csv", "w", encoding="utf-8") as file:
    #             writer = csv.writer(file)
    #             writer.writerow(
    #                 (
    #                     item_href,
    #                     item_art.group(0),
    #                     item_data,
    #                     item_price.group(0).replace(" ",""),
    #                     item_name.group(0)
    #                 )
    #             )





def main():
    # with open("all_categories_dict_for_radiators_and_elther.json", encoding="utf8") as file:
    #     all_categories = json.load(file)
    #
    # for item_text ,item_href_1 in all_categories.items():
    #     if len(item_text) > 20:
    #         url = f'{item_href_1}'
        url = 'https://leroymerlin.ru/catalogue/radiatory-otopleniya/'


        # print(url)
        useragents = open('useragents.txt').read().split('\n')
        proxies = open('proxies.txt').read().split('\n')
        # Создаем видимость что парсит человек и рандомизируем прокси и юзер агент
        for i in range(4):
            sleep(uniform(3, 12))
            proxy = {'http': 'http://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            try:
                html = get_html(url, useragent, proxy)
            except:
                continue
            try:
                get_ip(html)
            except AttributeError:
                continue
            pages_count = get_pages_count(html)
            print(pages_count)




if __name__ == '__main__':
    main()