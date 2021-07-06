from time import sleep
from datetime import datetime

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
                apartment = Apartment(title=title, location=location, price=price, date_time=date_time)
                if apartments.filter(Apartment.title == title, Apartment.location == location, Apartment.price == price,
                                     Apartment.date_time == date_time):
                    continue
                else:
                    new_apartments.append(apartment)
                    apartment.save()

            if new_apartments:
                for apartment in new_apartments:
                    message = f'Название: {apartment.title}. Цена: {apartment.price}. Местоположение: {apartment.location}. Время загрузки: {apartment.date_time}'
                    send_sms(message)
            else:
                print(f'Нет обновлений {datetime.now()}')
            sleep(TIME_SLEEP)
        except requests.exceptions.ConnectionError:
            print(f'Нет интернета {datetime.now()}!')
            sleep(TIME_SLEEP)
            continue
