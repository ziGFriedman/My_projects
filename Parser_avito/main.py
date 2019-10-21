import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)

def write_csv(data):
    with open('Parser_avito/avito.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title'],
                          data['price'],
                          data['url']) )

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended')

    for ad in ads:
        # title, price, url
        try:
            title = ad.find('div', class_='description item_table-description').find('a').get('title')
        except:
            title = ''

        try:
            price = ad.find('div', class_='description item_table-description').find('div', class_='about').find('span', class_='price').text.strip()
        except:
            price = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description item_table-description').find('a').get('href')
        except:
            url = ''

        data = {'title': title,
                'price': price,
                'url': url}

        write_csv(data)


def main():
    url = 'https://www.avito.ru/moskva/telefony/htc?p=1'
    base_url = 'https://www.avito.ru/moskva/telefony/htc?'
    page_part = 'p='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
