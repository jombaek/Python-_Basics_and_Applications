import requests
import json

with open(r'D:\Загрузки\dataset_24476_3.txt') as fin:
    for num in fin:
        num = num.strip()
        res = requests.get(f'http://numbersapi.com/{num}/math?json=true') 
        data = json.loads(res.content)

        if data['found']:
            print('Interesting')
        else:
            print('Boring')