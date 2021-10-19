import requests
from bs4 import BeautifulSoup
import csv, datetime

response = requests.get("https://e-kursy-walut.pl/")
soup = BeautifulSoup(response.text, 'html.parser')

crypto = ('Dupa', 'Bitcoin', 'Ethereum', 'Cardano', 'Binance Coin', 'Solana', 'BitTorrent', 'Ripple', 'Litecoin', 'Iota')

rows = []
for x in crypto:
    if not soup.find(text=x):
        continue
    else:
        usd_rate = soup.find(text=x).next_element.small.text
        pln_rate = soup.find(text=x).next_element.strong.text

        rows.append([x, usd_rate, pln_rate, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])


# zapis do pliku csv

filename = r'c:\temp\kursy.csv'
fields = ['Nazwa waluty', 'Kurs PLN', 'Kurs USD', 'Data + Time']

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
