import requests
from bs4 import BeautifulSoup
import os

paintingstyle = 1936

for p in range(1, 5):
    url = 'https://www.unique-poster.com/tableaux.html?p=' + str(p) + '&painting_style=' + str(paintingstyle) 
    #url = 'https://www.unique-poster.com/tableaux/styles-nouvelle-objectivite.html'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('li', attrs= {'class'  :'item product product-item-masonary'})

    for img in images:
        img_url = img.picture.source['srcset'].replace('.webp', '.jpg')
        img_name = img.a['title'].replace(' ', '_')
        print(img_url)
        if img_url.startswith("http"):
            img_data = requests.get(img_url).content
            with open(os.path.join('images', 'Nouvelle_Objectivité', img_name + '.jpg'), 'wb') as f:
                f.write(img_data)

