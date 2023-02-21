from bs4 import BeautifulSoup
import requests

def parse():
    URl = 'https://www.olx.kz/d/elektronika/igry-i-igrovye-pristavki/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

    }

    response = requests.get(URl, headers= HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'css-qfzx1y')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('h6', class_ = 'css-16v5mdi er34gjf0').get_text(strip = True)
        })

        for comp in comps:
            print(comp['title'])

parse()