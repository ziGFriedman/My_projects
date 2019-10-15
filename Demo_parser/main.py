from bs4 import BeautifulSoup
import re

def main():
    html = open ('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

# Парсинг сверху вниз
    # find
    # find_all

    div = soup.find_all('a')    # получим объект типо soup
    # div = soup.find('div', class_='links')    # Можно указывать параметры

    for a in div:   # найдем все ссылки в объекте soup
        link = a.get('href')
        print(link)

# Парсинг снизу вверх
    # parent = find_parent()    # метод find
    # parents = find_parents()    # метод find_all

    div = soup.find('h1').find_parent()    # Поиск родительского заголовка
    # div = soup.find('h1').find_parent('div', class_='class_name')    # Поиск конкретного родителя
    # div = soup.find('h1').find_parents('div')    # Поиск всех родителей, лучше ставить ограничения по параметрам
    print(div)

# Парсинг текста сверху вниз
    text = soup.find('h1').next_element    # Возвращяет следующий элемент
    # text = soup.find('h1').next
    # text = soup.find('h1').next_sibling    # Содержимое: после тэга h1 и до следующего тега.
    print(text)

# Парсинг текста снизу вверх
    text = soup.find('br').previous_sibling    # Предыдущий элемент

# Извлечение данных из тэга
    a = soup.find('a', href=re.compile('ya.ru'))    # Передаем, через регулярные выражения, строку (шаблон для идентификации ссылок)
    url = a.get('href')    # Передаем непосредственно ссылку из объекта soup
    print(url)

    div = soup.find('h1').parent    # родитель
    n = div.get('data-set')    # находим нужный атрибут тэга "12312312" в data-set, например:
    # <div>
    #   text
    #   <div data-set="12312312">
    #       <h1>
    #           Header
    #       </h1>

# Использование регулярных выражений для идентификации объектов
# <div class="links">
#     <a href="https://bing.com/first/1">Bing first post</a>
#     <a href="https://bing.com">Bing</a>    # Необходимо найти этот элемент
#     <a href="https://bing.com/second/2">Bing second post</a>
# </div>
    a = soup.find('a', href=re.compile('bing.com$'))    # $ - обозначает что дальше мы не ждем каких-либо символов
    # <a href="https://bing.com">Bing</a>
    a = soup.find('a', href=re.compile('2'))    # найдем 3-ю ссылку с атрибутом 2
    # <a href="https://bing.com/second/2">Bing second post</a>
    a = soup.find('a', text=re.compile('second'))    # поиск ссылки по тексту, по его анкору
    # <a href="https://bing.com/second/2">Bing second post</a>

# Поиск даты
# <div class="post">
#     <div>Content</div>
#     <div>2</div>
#     <div>3</div>
#
#     <div>16.01.2019</div>
# </div>
    # 16.01.2019
    regexp = r'\d{2}.\d{2}.\d{4}'    # Установим регулярное выражение по структуре даты
    # r'\w' - (буквы цифры _)
    # r'\w\-' - (буквы цифры _ -)
    # r'^' -  Начинается с ... например r'^post' - начинается с post
    # r'/\d{1}$' - строка с 1 цифрой ($ - последуюзие символы)

    a = soup.find('div', text=re.compile(regexp))
    # <div>16.01.2019</div>
    a = soup.find(text=re.compile(regexp))    # Найдет первый попавшийся текст с такими атрибутами регулярного выражения
    # 16.01.2019

if __name__ == '__main__':
    main()
