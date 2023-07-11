import config
import requests
import json

client_id = config.client_id
client_secret = config.client_secret

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

artists = []

with open(r'D:\Загрузки\dataset_24476_4.txt', 'r') as fin:
    for artist_id in fin:
        # инициируем запрос с заголовком
        r = requests.get(f"https://api.artsy.net/api/artists/{artist_id.strip()}", headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        artists.append({'name': j['sortable_name'], 'birthday': j['birthday']})

for artist in sorted(artists, key=lambda x : (x['birthday'], x['name'])):
    print(artist['name'])