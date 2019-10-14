import requests
from bs4 import BeautifulSoup

r = requests.get('http://startapy.ru/')
soup = BeautifulSoup(r.text, 'lxml')

uls = soup.find_all('ul', class_='mcol')

ul = uls[0]
lis = ul.find_all('li')

with open('Parser_startapy/output.txt', 'w') as file:
    file.write(str(lis))
file.close()
