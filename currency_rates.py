import requests
from bs4 import BeautifulSoup
from datetime import datetime


def currency_rates(currency):
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.content, 'xml')

    if soup.find('CharCode', text=currency) == None:
        return print(f'Валюты {currency} не существует')
    else:
        result = float(((soup.find('CharCode', text=currency).find_next_sibling('Value').string)).replace(',', '.'))
        currency_name = (soup.find('CharCode', text=currency).find_next_sibling('Name').string)
        datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return print(f'На {datetime_now} {currency_name} по отношеню к рублю равен {result:.2f}')


