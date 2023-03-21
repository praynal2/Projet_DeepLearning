import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.unique-poster.com/tableaux/styles-d-art-baroque.html'  # Baroque
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('picture/img')
#print(images)

if not os.path.exists('images/Baroque'):
    os.makedirs('images/Baroque')

for img in images:
    img_url = img['src']
    img_name = img['alt']
    img_data = requests.get(img_url).content
    with open('images/Baroque' + img_name, 'wb') as handler:
        handler.write(img_data)
