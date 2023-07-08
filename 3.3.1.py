import requests
import re

a = input().replace('stepic.org', 'stepik.org')
b = input().replace('stepic.org', 'stepik.org')

pattern = r'<a[^>]*?href="(.*?)"[^>]*?>'

def check(url1, url2):
    # Загрузка HTML-кода документа A
    response_a = requests.get(url1)
    html_a = response_a.text.replace('stepic.org', 'stepik.org')

    # Поиск ссылок внутри документа A
    links_a = re.findall(pattern, html_a)

    # Проверка каждой ссылки в документе A
    for link_a in links_a:
        # Загрузка HTML-кода документа C
        response_c = requests.get(link_a)
        html_c = response_c.text.replace('stepic.org', 'stepik.org')

        # Поиск ссылок внутри документа C
        links_c = re.findall(pattern, html_c)

        # Проверка каждой ссылки в документе C
        for link_c in links_c:
            if url2 in link_c:
                return 'Yes'

    return 'No'

print(check(a, b))