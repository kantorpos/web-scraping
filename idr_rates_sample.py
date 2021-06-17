import requests

# json_data = requests.get('https://floatrates.com/daily/idr.json')
json_data = {
    'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.9872761309769e-05,
            'date': 'Thu, 17 Jun 2021 11:55:01 GMT', 'inverseRate': 14311.728651551},
    'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.7729003867666e-05,
            'date': 'Thu, 17 Jun 2021 11:55:01 GMT', 'inverseRate': 17322.315179599}}
print(json_data)

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
