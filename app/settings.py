import os

from dotenv import load_dotenv

load_dotenv()

PHONE_NUMBER_FROM = os.environ['TWILIO_NUMBER_FROM']
PHONE_NUMBER_TO = os.environ['NUMBER_TO']
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

URL = os.environ['URL']
DATE_TIME_START = '2021-06-06 00:00:00'  # %Y-%m-%d %H:%M:%S
TIME_SLEEP = 30

USER = os.environ['MYSQL_USER']
PASSWORD = os.environ['MYSQL_PASSWORD']
DB_NAME = 'apartment'
