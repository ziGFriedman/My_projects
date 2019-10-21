import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)

def main():
    url = 'https://www.avito.ru/moskva/telefony/htc?p=1'
    base_url = 'https://www.avito.ru/moskva/telefony/htc?'
    page_part = 'p='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i)
        


if __name__ == '__main__':
    main()
