# OrthodoxCalendar.py
# Grabs the Gregorian/Julian date, description, whether or not it's a fasting day, and the daily scripture readings. 
# Mason Whitaker
# Created: 07/04/2024
# Updated: 07/08/2024

import requests
import os
from requests_html import HTMLSession
import requests
import textwrap

url = "https://www.holytrinityorthodox.com/calendar/calendar.php"

try:
    session = HTMLSession()
    response = session.get(url)
    
except requests.exceptions.RequestException as e:
    print(e)

os.system('cls||clear')

date = response.html.find('.pdataheader',first=True)
date_fasting = response.html.find('.pheaderheader',first=True)
scripture = response.html.find('.normaltext')
scripture = scripture[1]
passages = scripture.text.splitlines()

print("\n")
print(date.text,"\n")
print(date_fasting.text,"\n")

width = 120

for citation in passages:
    book = citation.split(' ', 1)[0]
    chapter = citation.split(' ',2)[1]
    chapter = chapter.replace(',', '')
    chapter = chapter.replace(';', '')

    response = requests.get(str('https://bible-api.com/' + str(book) + str(chapter) +'?translation=kjv'))
    data = response.json()
    response_reference = data['reference']
    response_text = textwrap.fill(data['text'], width=width)
    response_text = response_text.replace('           ', '')
    print(response_reference,"\n\n\t",response_text,"\n\n")
    

input("Press enter to exit...")

