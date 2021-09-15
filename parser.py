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



def get_ip(html):
    soup = BeautifulSoup(html, "lxml")
    all_products_hrefs = soup.find_all("a", class_="bex6mjh_plp")

    all_categories_dict_for_radiators_and_elther = {}
    for item in all_products_hrefs:
        item_text = item.text
        item_href_1 = 'https://leroymerlin.ru/' + item.find_next('a').get("href")
        # print(item_href_1)
        all_categories_dict_for_radiators_and_elther[item_text] = item_href_1

    with open("all_categories_dict_for_radiators_and_elther.json", "w", encoding='utf8') as file:
        json.dump(all_categories_dict_for_radiators_and_elther, file, indent=4, ensure_ascii=False)
    print('---'*20)

    # print('New proxy & New UserAgent:')
    # soup = BeautifulSoup(html, 'lxml')
    # all_products_hrefs = soup.find_all("div", class_ = "phytpj4_plp")
    # all_categories_dict_rad_stal = {}
    # for item in all_products_hrefs:
    #     item_art = re.search('\d{8}', item.text)
    #     if item_art:
    #         item_art.group(0)
    #     item_href = 'https://leroymerlin.ru' + item.find_next('a').get('href')
    #     item_name = re.search(item.text[13:80], item.text)
    #     item_data = datetime.now()
    #     item_price = re.search('\d{1}\s\d{3}\s₽/шт|\d{2}\s\d{3}\s₽/шт', item.text)
    #     for_adding = all_categories_dict_rad_stal[item_art.group(0)] = item_name.group(0), item_href, item_data, item_price.group(0).replace(" ","")
    #
    #     with open(f"data/{item_text}.csv", "w", encoding="utf-8") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(
    #             (
    #                 item_href,
    #                 item_art.group(0),
    #                 item_data,
    #                 item_price.group(0).replace(" ",""),
    #                 item_name.group(0)
    #             )
    #         )





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



# Создание точки входа
if __name__ == '__main__':
    main()

#
#
#
#
# # url = "https://leroymerlin.ru/catalogue/radiatory-otopleniya/"
# # url_1 = "https://leroymerlin.ru/catalogue/radiatory-stalnye/" # Для одного радиатора
# # Для того, чтобы сайт не думал что я бот и не забанил
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
#
# }
#
# # Сохранить страницу для дальнейшего парсинга данных
# # req = requests.get(url, headers=headers)
# # src = req.text
# # with open("index_rollback.html", "w", encoding = 'utf8') as file:
# #     file.write(src)
#
#
#
#
#
# # Получение списка радиаторов
# # with open("index_rollback.html", encoding='utf8') as file:
# #     src = file.read()
# # soup = BeautifulSoup(src, "lxml")
# # all_products_hrefs = soup.find_all("a")
# # all_categories_dict = {}
# # for item in all_products_hrefs:
# #     item_text = item.text
# #     item_href = "https://leroymerlin.ru" + item.get("href")
# #     all_categories_dict[item_text] = item_href
# # with open("all_categories_dict_rollback.json", "w", encoding='utf8') as file:
# #     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
#
#
#
#
#
#
#
# # Сокращаем список из радиаторов до одного (преобразование в список и по индексу берем)
# # with open("all_categories_dict_rollback.json", encoding = "utf8") as file:
# #     all_categories_rollback = json.load(file)
# # data = dict(all_categories_rollback)
# # items = list(data.items())
# # all_categories_rollback_1 = items[10:11] # взяли несколько рандомных радиаторов
#
#
#
#
# # В категории одного радиатора создаем html страничку
# # req = requests.get(url_1, headers=headers)
# # src = req.text
# # with open("index_rollback_radiators_stal.html", "w", encoding = 'utf8') as file:
# #     file.write(src)
#
#
# # В категории одного радиатора находим список товаров
# # with open("index_rollback_radiators_stal.html", encoding='utf8') as file:
# #     src = file.read()
# # soup = BeautifulSoup(src, "lxml")
# # all_products_hrefs = soup.find_all("a")
# # all_categories_dict_rad_stal = {}
# # for item in all_products_hrefs:
# #     item_text = item.text
# #     item_href = "https://leroymerlin.ru/catalogue/radiatory-stalnye" + item.get("href")
# #     all_categories_dict_rad_stal[item_text] = item_href
# # with open("all_categories_dict_rad_stal.json", "w", encoding='utf8') as file:
# #     json.dump(all_categories_dict_rad_stal, file, indent=4, ensure_ascii=False)
#
#
#
# # Из полученного списка выбираем ПЯТЬ элемент
# # with open("all_categories_dict_rad_stal.json", encoding = "utf8") as file:
# #     all_categories_dict_rad_stal = json.load(file)
# # data = dict(all_categories_dict_rad_stal)
# # items = list(data.items())
# # all_categories_dict_rad_stal_1 = items[10:15] # взяли несколько рандомных радиаторов
# # with open("all_categories_dict_rad_stal_1.json", "w", encoding='utf8') as file:
# #     json.dump(all_categories_dict_rad_stal_1, file, indent=4, ensure_ascii=False)
#
#
#
#
#
# # Редактируем список, который сделали выше
# with open("all_categories_dict_rad_stal_1.json", encoding = "utf8") as file:
#     all_categories_dict_rad_stal_1 = json.load(file)
# count = 0
# for category_name, category_href in all_categories_dict_rad_stal_1:
#     if count == 0:
#     # Код для замены нескольких символов сразу
#     #     rep = [",", " ", "-", "'", "\n"]
#     #     for item in rep:
#     #         if item in category_name:
#     #             category_name = category_name.replace(item, "_")
#         req = requests.get(url=category_href, headers=headers)
#         src = req.text
#
#         # with open(f"data/{count}_{category_name}_rad_stal.html", "w", encoding = "utf8") as file:
#         #     file.write(src)
#
#
# # Сбор данных
# #         with open(f"data/{count}_{category_name}_rad_stal.html", "r", encoding = "utf8") as file:
# #             src = file.read()
#         soup =  BeautifulSoup(src, "lxml")
#         table_head = soup.find_all("title")
#         print(table_head)
#
#
# count += 1





# Собираем нужные нам данные с этого элемента

















# # #     iteration_count = int(len(all_categories)) - 1
# count = 0
# #     print(f"Всего итераций: {iteration_count}")
# for category_name, category_href in all_categories_rollback_1:
#     if count == 0:
#     # Код для замены нескольких символов сразу
#         rep = [",", " ", "-", "'", "\n"]
#         for item in rep:
#             if item in category_name:
#                 category_name = category_name.replace(item, "_")
#             # print(category_name)
#
#         req = requests.get(url=category_href, headers=headers)
#         src = req.text
#     #
#         with open(f"data/{count}_{category_name}_rollback.html", "w", encoding = "utf8") as file:
#             file.write(src)
#
#
#     with open(f"data/{count}_{category_name}.html", encoding = 'utf-8') as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, "lxml")
#     all_products_radiators_hrefs = soup.find_all("a")
#     #
#
#     # all_p
#     all_categories_dict_rollback_radiators = {}
#     for item in all_products_radiators_hrefs:
#         item_text_radiators = item.text
#         item_href_radiators = "'https://leroymerlin.ru/catalogue/radiatory-stalnye" + item.get("href")
#     #
#     #
#     #
#     #
#         all_categories_dict_rollback_radiators[item_text_radiators] = item_href_radiators
#
#         with open("all_categories_dict_rollback_radiators.json", "w", encoding='utf8') as file:
#             json.dump(all_categories_dict_rollback_radiators, file, indent=4, ensure_ascii=False)
#
#         count += 1



#     # Проверим что выходит на одной странице чтобы не бомбить сайт
#
#
    # with open(f"data/{count}_{category_name}.html", encoding = 'utf-8') as file:
    #     src = file.read()


    # soup = BeautifulSoup(src, "lxml")


#
#     # проверка страницы на наличие таблицы с продуктами
#     alert_block = soup.find(class_="uk-alert-danger")
#     if alert_block is not None:
#         continue
#
#     # собираем заголовки таблицы
#     table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
#
#
#     product = table_head[0].text
#     calories = table_head[1].text
#     proteins = table_head[2].text
#     fats = table_head[3].text
#     carbohydrates = table_head[4].text
#
#
#     with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 product,
#                 calories,
#                 proteins,
#                 fats,
#                 carbohydrates
#             )
#         )
#
#     # собираем данные продуктов
#     products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
#
#     product_info = []
#     for item in products_data:
#         product_tds = item.find_all("td")
#
#
#         title = product_tds[0].find("a").text
#         calories = product_tds[1].text
#         proteins = product_tds[2].text
#         fats = product_tds[3].text
#         carbohydrates = product_tds[4].text
#
#
#         product_info.append(
#             {
#                 "Title": title,
#                 "Calories": calories,
#                 "Proteins": proteins,
#                 "Fats": fats,
#                 "Carbohydrates": carbohydrates
#             }
#         )
#         with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     title,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )
#             )
#     with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
#         json.dump(product_info, file, indent=4, ensure_ascii=False)
#
#     count += 1
#     print(f"# Итерация {count}. {category_name} записан...")
#     iteration_count = iteration_count - 1
#
#     if iteration_count == 0:
#         print("Работа завершена")
#         break
#
#     print(f"Осталось итераций: {iteration_count}")
#     sleep(random.randrange(2, 4))
