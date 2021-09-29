import requests
from bs4 import BeautifulSoup


def save():
    with open('nbkr.txt', 'a') as file:
        file.writelines(f"id: {comp['id']}Hаименование банка: {comp['namebank']},Почтовый адрес, телефон: {comp['adress']}, Ф.И.О Председателя банка (Руководителя филиала): {comp['fio']} : {comp['nal']}, Кол-во филиалов: {comp['kf']}, Электронная почта, веб-сайт:{comp['pocad']}")


def parse():
    URL = 'https://www.nbkr.kg/index1.jsp?item=69&lang=RUS'
    HEADERS = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }

    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ ='table-responsive')
    comps = []
    print(items)

    for item in items:
        try:
            comps.append({
        'namebank': item.find('td', width_ = '20%').find('text', style_ = 'font-weight: 700;').get_text(strip=True),
        'adress': item.find('td', width_ = '22%').find('text', style_ = 'font-weight: 700').get_text(strip=True),
        'fio': item.find('td', width_ = '18%').find('text', style_ = 'font-weight: 700;').get_text(strip=True),
        'kf': item.find('td', width_ = '8%').find('text', style_ = 'font-weight: 700;').get_text(strip=True),
        'pocad': item.find('td', width_ = '23%').find('text', style_ = 'font-weight: 700;').get_text(strip=True)
       })
        except:
            pass
    global comp
    for comp in comps:
        print(f"id: {comp['id']}Hаименование банка: {comp['namebank']},Почтовый адрес, телефон: {comp['adress']}, Ф.И.О Председателя банка (Руководителя филиала): {comp['fio']} : {comp['nal']}, Кол-во филиалов: {comp['kf']}, Электронная почта, веб-сайт:{comp['pocad']}")
        save()
parse()