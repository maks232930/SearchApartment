import re
from datetime import datetime


MONTHS = ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


def get_date_time_in_normal_format(date_time):
    date_time = date_time.replace(',', '').replace('.', '')
    now = datetime.now()

    if 'Вчера' in date_time or 'Сегодня' in date_time:
        if 'Сегодня' in date_time:
            return datetime.strptime(f'{now.year}-{now.month}-{now.day} {date_time[7:]}:00', '%Y-%m-%d %H:%M:%S')
        else:
            return datetime.strptime(f'{now.year}-{now.month}-{now.day - 1} {date_time[5:]}:00', '%Y-%m-%d %H:%M:%S')
    else:
        month = re.findall(r'\w{3}', date_time)[0]

        day = re.findall(r'\d{1,2}', date_time[:2])[0]

        return datetime.strptime(f'{now.year}-{MONTHS.index(month)}-{day} {date_time[-5:]}:00', '%Y-%m-%d %H:%M:%S')
