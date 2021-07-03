from twilio.rest import Client

from app.settings import ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER_FROM, PHONE_NUMBER_TO


def send_sms(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(body=message, to=PHONE_NUMBER_TO, from_=PHONE_NUMBER_FROM)
