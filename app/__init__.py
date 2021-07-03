from time import sleep

import requests

from app.models import Apartment
from app.parser_apartments import get_apartments
from app.settings import URL, TIME_SLEEP
from app.sms import send_sms


def run():
    while True:
        try:
            new_apartments = []
            now_apartments = get_apartments(URL)

            apartments = Apartment.select()

            for title, price, location, date_time in now_apartments:
                apartment = Apartment(id=title, location=location, price=price, date_time=date_time)
                if apartments.filter(Apartment.title == title, Apartment.location == location, Apartment.price == price,
                                     Apartment.date_time == date_time):
                    continue
                else:
                    if apartment.title is None:
                        continue

                    new_apartments.append(apartment)
                    apartment.save()

            if new_apartments:
                for apartment in new_apartments:
                    message = f'Название: {apartment.title}. Цена: {apartment.price}. Местоположение: {apartment.location}. Время загрузки: {apartment.date_time}'
                    send_sms(message)
            else:
                print('Нет обновлений')
            sleep(TIME_SLEEP)
        except requests.exceptions.ConnectionError:
            print('Нет интернета!')
            sleep(TIME_SLEEP)
            continue
