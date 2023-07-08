import requests
import re
from urllib.parse import urlparse

pattern = r'<a[^>]*?href="(.*?)"[^>]*?>'

link = input()
links = re.findall(pattern, requests.get(link).text)

res = set()

for link  in links:
    parsed_url = urlparse(link)
    domain = parsed_url.netloc
    if parsed_url.port is None:
        res.add(domain)

res = sorted(res)
for i in res:
    print(i)