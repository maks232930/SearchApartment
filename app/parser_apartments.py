from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from lxml import html

from app.utils import get_date_time_in_normal_format


def get_html_apartments(url):
    response = requests.get(url)

    tree = html.document_fromstring(response.text)
    while True:
        try:
            title_class = \
                tree.xpath('/html/body/div[1]/div/div[1]/main/div/div/div[3]/div[1]/article/div/div/a[1]/div[2]/div[3]')[
                    0].attrib.values()[0]
            price_class = tree.xpath(
                '/html/body/div[1]/div/div[1]/main/div/div/div[3]/div[1]/article/div/div/a[1]/div[2]/div[1]/div[1]')[
                0].attrib.values()[0]
            location_class = \
                tree.xpath(
                    '/html/body/div[1]/div/div[1]/main/div/div/div[3]/div[1]/article/div/div/a[1]/div[2]/div[4]/span')[
                    0].attrib.values()[0]
            date_time_class = \
                tree.xpath('/html/body/div[1]/div/div[1]/main/div/div/div[3]/div[1]/article/div/div/a[1]/div[1]/div[2]')[
                    0].attrib.values()[0]

            class_list = [title_class, price_class, location_class, date_time_class]

            apartments = bs(response.content, 'lxml').find('article').find('div').find('div').find_all('a')

            return apartments, class_list
        except IndexError:
            print(f'Произошла ошибка! Ждем 30 сек')
            sleep(30)
            print('Продолжаем')
            continue


def get_apartments(url):
    apartments, class_list = get_html_apartments(url)
    apartments_list = []

    for apartment in apartments:
        title = apartment.find('div', attrs={'class': class_list[0]}).text
        price = apartment.find('div', attrs={'class': class_list[1]}).find_all('span')[-1]
        if price is None:
            price = 'Договорная'
        else:
            price = price.text[:-11].replace(' ', '')
        location = apartment.find('span', attrs={'class': class_list[2]}).text
        date_time = get_date_time_in_normal_format(
            apartment.find('div', attrs={'class': class_list[3]}).find('span').text)

        apartments_list.append([title, price, location, date_time])
    return apartments_list
