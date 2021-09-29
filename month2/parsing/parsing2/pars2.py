import requests
from bs4 import BeautifulSoup


def save():
    with open('sulpak.txt', 'a') as file:
        file.writelines(f"Название: {comp['title']}, Цена: {comp['price']}")


def parse():
    URL = 'https://www.sulpak.kg/f/planshetiy'
    HEADERS = {
        'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
        'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }

    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ ='goods-tiles')
    comps = []
    print(items)

    for item in items:
        try:
            comps.append({
                'title': item.find('h3', class_ = 'title').get_text(strip=True),
                'image': item.find('img',class_ = 'image-size-cls').get_text(strip=True),
                'price': item.find('div',class_ = 'price' ).get_text(strip=True),
                'nal': item.find('span',class_ = 'availability').get_text(strip=True),
                'kodtav': item.find('span',class_ = 'code').get_text(strip=True),
                'pokupka': item.find('div',class_ = 'red-btn bg-transition buy-btn enhancement-ecommers-buy buy-btn-right').get_text(strip=True),
                'rei': item.find('i',class_ = 'fa fa-star active').get_text(strip=True),
                'otzv': item.find('span',class_= 'coments-quantity').get_text(strip=True)
        })
        except:
            pass
    global comp
    for comp in comps:
        print(f"Название: {comp['title']},Фотки: {comp['image']}, Цена: {comp['price']} Наличии: {comp['nal']}, Код товара: {comp['kodtav']}, Купить: {comp['pokupka']}, Рейтинг: {comp['rei']}, Отзывы: {comp['otzv']}")
        save()
parse()


    