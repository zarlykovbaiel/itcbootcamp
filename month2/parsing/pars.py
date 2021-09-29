import requests
from bs4 import BeautifulSoup
import csv

CSV = 'parser.csv'
HOST = 'https://www.kivano.kg/'
URL = 'https://www.kivano.kg/noutbuki'
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'User-Agent:Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# html = get_html(URL)
# print(html)
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'item product_listbox oh')
    new_list = []
    
    for item in items:
        new_list.append({
            'title': item.find('div', class_ = 'product_text pull-left').find('div', class_ = 'listbox_title oh').find('a').get_text(strip=True),
            'image': HOST + item.find('div', class_ = 'listbox_img pull-left').find('img').get('src'),
            'price': item.find('div', class_ = 'listbox_price text-center').get_text(strip=True),
            'nalichie': item.find('div', class_ = 'listbox_motive text-center').get_text(strip=True),
            'basket': item.find('div', class_ = 'more4 pull-left').get_text(strip=True),
            'kredit': item.find('div', class_ = 'more5 pull-right').get_text(strip=True),
            'pokupka': item.find('div', class_ = 'oh ib').get_text(strip=True)
        })

    return new_list

def save(items, path):
    with open(path , 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название', 'Фотки', 'Цена', 'Наличии', 'Корзина', 'Kредит', 'Покупка'])
        for item in items :
            writer.writerow([item['title'], item['image'], item['price'], item['nalichie'], item['basket'], item['kredit'], item['pokupka']])




def parser():
    PAGINATION = input('Введите кол-во страниц: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        new_list=[]
        for page in range(1, PAGINATION):
            print(f'Страница №{page} Готова!')
            html = get_html(URL, params={'page': page})
            new_list.extend(get_content(html.text))
        save(new_list,CSV)
        print('Парсинг готов!')
    else:
        print('Ошибка')

parser()

















