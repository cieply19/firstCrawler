import requests
from bs4 import BeautifulSoup
import csv, datetime

response = requests.get("https://e-kursy-walut.pl/")
soup = BeautifulSoup(response.text, 'html.parser')

crypto = (
'Dupa', 'Bitcoin', 'Ethereum', 'Cardano', 'Binance Coin', 'Solana', 'BitTorrent', 'Ripple', 'Litecoin', 'Iota')

rows = []
for x in crypto:
    if not soup.find(text=x):
        continue
    else:
        usd_rate = soup.find(text=x).next_element.small.text
        pln_rate = soup.find(text=x).next_element.strong.text

        rows.append({'Nazwa waluty': x, 'Kurs USD': usd_rate, 'Kurs PLN': pln_rate,
                     'Data + Czas pobrania kursu': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

# zapis do pliku csv

filename = 'kursy.csv'
fields = ['Nazwa waluty', 'Kurs USD', 'Kurs PLN', 'Data + Czas pobrania kursu']

with open(filename, 'a') as csvfile:
    csvwriter = csv.DictWriter(csvfile, ('Nazwa waluty', 'Kurs USD', 'Kurs PLN', 'Data + Czas pobrania kursu'))
    if not csvfile.tell():
        csvwriter.writeheader()

    csvwriter.writerows(rows)
