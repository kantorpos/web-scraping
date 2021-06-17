import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-populer')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(html_doc.text, "html.parser")
    tag_terpopuler = soup.find(attrs={'class': 'grid-row list-content'})
    images = tag_terpopuler.findAll(attrs={'class': 'media__link'})
    return render_template('detik-scraper.html', images=images)


@app.route('/idr-rates')
def idr_rates():
    source = requests.get('https://floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())


if __name__ == '__main__':
    app.run(debug=True)
