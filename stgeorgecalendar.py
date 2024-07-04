import requests
import os
from requests_html import HTMLSession

url = "https://stgeorgeroc.org/category/schedules/"

try:
    session = HTMLSession()
    response = session.get(url)
    
except requests.exceptions.RequestException as e:
    print(e)

date = response.html.find('.entry-content',first=True).text
date = date.splitlines()
os.system('cls||clear')
for item in date:
    print(item)