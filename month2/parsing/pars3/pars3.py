from bs4 import BeautifulSoup
import requests
import csv
CSV = 'minfin.csv'
HOST = 'http://www.minfin.kg/'
URL = 'http://www.minfin.kg/ru/novosti/mamlekettik-karyz/gosudarstvennyy-dolg'
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}



def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, verify=False, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'news')
    new_list = []
    for item in items:
        new_list.append({
        'data': item.find('div', class_ = 'news_date').get_text(strip=True),
        'title': item.find('div', class_ = 'news_name').get_text(strip=True),
        'news': item.find('div', class_ = 'news_anons').get_text(strip=True),
        'link': HOST+item.find('div', class_ = 'news_name').find('a').get('href')
        # 'image': item.find('image', src  = '').get_text(strip=True),

        })
    return new_list

def new_save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Дата', 'Название', 'Новости', 'Ссылка'])
        for item in items:
            writer.writerow([item['data'], item['title'], item['news'], item['link']])

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