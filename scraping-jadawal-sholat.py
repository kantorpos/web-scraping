import bs4
import requests

url = 'http://www.jadwalsholat.pkpu.or.id/?id=83'
contents = requests.get(url)
print(contents)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = (data[0])
print(f"Data dari PKPU {data}")
print(f"Data mentah {data.get_text()}")

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['magrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1

print(f"Jadwal sholat hari ini : {sholat}")
print(f"Jadwal Sholat Ashar : '{sholat['ashar']}")