# OrthodoxCalendar.py
# Grabs the Gregorian/Julian date, description, whether or not it's a fasting day, and the daily scripture readings. 
# Mason Whitaker
# 07/04/2024

import requests
from requests_html import HTMLSession

url = "https://www.holytrinityorthodox.com/calendar/calendar.php"

try:
    session = HTMLSession()
    response = session.get(url)
    
except requests.exceptions.RequestException as e:
    print(e)

date = response.html.find('.pdataheader',first=True)
date_fasting = response.html.find('.pheaderheader',first=True)
scripture = response.html.find('.normaltext')
scripture = scripture[1]

print("\n")
print(date.text,"\n")
print(date_fasting.text,"\n")
print(scripture.text,"\n")

