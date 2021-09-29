from bs4 import BeautifulSoup
import requests
import csv
CSV = 'wild.csv'
HOST = 'https://kg.wildberries.ru/'
URL = 'https://kg.wildberries.ru/catalog/muzhchinam/odezhda/verhnyaya-odezhda'
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, verify=False, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'product-card__wrapper')
    new_list = []
    for item in items:
        new_list.append({
        
        'img': item.find('div', class_ = 'product-card__img-wrap').get_text(strip=True),
        'price': item.find('ins', class_ = 'lower-price').get_text(strip=True),
        'sale': item.find('span', class_ = 'price').get_text(strip=True),
        'brand': item.find('strong', class_ = 'brand-name').get_text(strip=True),
        'title': item.find('span', class_ = 'goods-name').get_text(strip=True)



        })

        return new_list

def new_save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Изображение', 'Цена', 'Скидка', 'Бренд', 'Название'])
        for item in items:
            writer.writerow([item['img'], item['price'], item['sale'], item['brand'], item['title']])

def parce():
    PAGINATOR = input('Введите кол-во страниц: ')
    PAGINATOR = int(PAGINATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        new_list=[]
        for page in range(1, PAGINATOR):
            print(f'Страница №{page} Готова!')
            html = get_html(URL, params={'page': page})
            new_list.extend(get_content(html.text))
            new_save(new_list, CSV)
        print('Парсинг готов!')
    else:
        print('Чини код!')

parce()