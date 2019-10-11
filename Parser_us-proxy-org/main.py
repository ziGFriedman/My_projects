# pip install bs4
# pip install lxml
# pip install requests

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.us-proxy.org/')
soup = BeautifulSoup(r.text, 'lxml')

trs = soup.find('table', id='proxylisttable').find('tbody').find_all('tr')

with open('Parser_us-proxy-org/output.txt', 'w') as file:
    file.write(str(trs))
file.close()
