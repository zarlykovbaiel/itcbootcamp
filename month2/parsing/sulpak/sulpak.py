import requests
from bs4 import BeautifulSoup
import csv

CSV = 'parser.scv'
HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/ff/planshetiy'
HEADERS = {
    'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'

}

def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, verify=False, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'goods-tiles')
    new_list = []
    
    for item in items:
        new_list.append({
                'title': item.find('h3', class_ = 'goods-titles').find('div', class_ = 'title').find('a').get_text(strip=True),
                'image': HOST + item.find('img',class_ = 'image-size-cls').find('img').get('src'),
                'price': item.find('div',class_ = 'price' ).get_text(strip=True),
                'nal': item.find('span',class_ = 'availability').get_text(strip=True),
                'kodtav': item.find('span',class_ = 'code').get_text(strip=True),
                'pokupka': item.find('div',class_ = 'red-btn bg-transition buy-btn enhancement-ecommers-buy buy-btn-right').get_text(strip=True),
                'rei': item.find('i',class_ = 'fa fa-star active').get_text(strip=True),
                'otzv': item.find('span',class_= 'coments-quantity').get_text(strip=True)
        })
        
    return new_list

def save(items, path):
    with open(path , 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название', 'Фотки', 'Цена', 'Наличии', 'Код товара', 'Покупка', 'Рейтинг', 'Отзывы'])
        for item in items :
            writer.writerow([item['title'], item['image'], item['price'], item['nal'], item['kodtav'], item['pokupka'], item['rei'], item['otzv']])




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
        print('Исправляй код')

parser()














# from home.baiel.parsing.pars import CSV
# import requests
# from bs4 import BeautifulSoup
# import csv

# CSV = 'sula.csv'
# def save():
#     with open('sulpak.csv', 'a') as file:
#         file.writelines(f"Название: {comp['title']},Фотки: {comp['image']}, Цена: {comp['price']} Наличии: {comp['nal']}, Код товара: {comp['kodtav']}, Купить: {comp['pokupka']}, Рейтинг: {comp['rei']}, Отзывы: {comp['otzv']}")


# def parser():
#     URL = 'https://www.sulpak.kg/f/planshetiy'
#     HEADERS = {
#         'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
#         'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
#     }

#     response = requests.get(URL, headers=HEADERS, verify=False)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     items = soup.find_all('div', class_ ='goods-tiles')
#     comps = []
#     print(items)

#     for item in items:
#         new_list = []
#         try:
#             comps.append({
#                 'title': item.find('h3', class_ = 'title').get_text(strip=True),
#                 'image': item.find('img',class_ = 'image-size-cls').get_text(strip=True),
#                 'price': item.find('div',class_ = 'price' ).get_text(strip=True),
#                 'nal': item.find('span',class_ = 'availability').get_text(strip=True),
#                 'kodtav': item.find('span',class_ = 'code').get_text(strip=True),
#                 'pokupka': item.find('div',class_ = 'red-btn bg-transition buy-btn enhancement-ecommers-buy buy-btn-right').get_text(strip=True),
#                 'rei': item.find('i',class_ = 'fa fa-star active').get_text(strip=True),
#                 'otzv': item.find('span',class_= 'coments-quantity').get_text(strip=True)
#         })
#         except:
#             pass
#     global comp
#     for comp in comps:
#         print(f"Название: {comp['title']},Фотки: {comp['image']}, Цена: {comp['price']} Наличии: {comp['nal']}, Код товара: {comp['kodtav']}, Купить: {comp['pokupka']}, Рейтинг: {comp['rei']}, Отзывы: {comp['otzv']}")
#         save(new_list,CSV)


# parser()
