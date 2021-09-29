from bs4 import BeautifulSoup
import requests
import csv
CSV = 'nbkr.csv'
HOST = 'https://www.nbkr.kg/'
URL = 'https://www.nbkr.kg/index1.jsp?item=69&lang=RUS'
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'table-responsive')
    new_list = []
    for item in items:
        new_list.append({
        'namebank': item.find('td', class_ = '20%').find('text', class_ = 'font-weight: 700;').get_text(strip=True),
        'adress': item.find('td', class_ = '22%').find('text', class_ = 'font-weight: 700').get_text(strip=True),
        'fio': item.find('td', class_ = '18%').find('text', class_ = 'font-weight: 700;').get_text(strip=True),
        'kf': item.find('td', class_ = '8%').find('text', class_ = 'font-weight: 700;').get_text(strip=True),
        'pocad': item.find('td', class_ = '23%').find('text', class_ = 'font-weight: 700;').get_text(strip=True)

    })

        return new_list

def new_save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Наименование банка', 'Почтовый адрес, телефон', 'Ф.И.О Председателя банка (Руководителя филиала)', 'Кол-во филиалов', 'Электронная почта, веб-сайт'])
        for item in items:
            writer.writerow([item['namebank'], item['adress'], item['fio'], item['kf'], item['pocad']])

def parce():
    PAGINATOR = input('Введите кол-во страниц: ')
    PAGINATOR = int(PAGINATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        new_list=[]
        for page in range(1, PAGINATOR):
            print(f'Страница №{page} Готова!')
            html = get_html(URL, params={'page': page})
            new_list.extend(get_content((html.text)))
            new_save(new_list, CSV)
        print('Парсинг готов!')
    else:
        print('Чини код!')

parce()