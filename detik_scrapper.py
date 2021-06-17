import bs4
import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/tag/bangkit-dari-corona', params={'tag_from': 'wp_tagpopuler'})
soup = BeautifulSoup(html_doc.text, "html.parser")
tag_terpopuler = soup.find(attrs={'class': 'l_content'})
titles = tag_terpopuler.findAll(attrs={'class': 'title'})

for title in titles:
    print(title.get_text())

images = tag_terpopuler.findAll(attrs={'class': 'ratiobox_content lqd'})

for image in images:
    print(image.find('img')['src'])

