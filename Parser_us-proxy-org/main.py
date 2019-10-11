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

with open('Parser_us-proxy-org/output.txt', 'r') as file1:
    str = file1.read()
    a = tuple(str.split(','))
    with open('Parser_us-proxy-org/output2.txt', 'w') as file2:
        for i in a:
            file2.write(i + '\n')
    file2.close()
file1.close()
