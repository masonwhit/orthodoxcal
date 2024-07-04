# OrthodoxCalendar.py
# Grabs the Gregorian/Julian date, description, whether or not it's a fasting day, and the daily scripture readings. 
# Mason Whitaker
# 07/04/2024

import requests
import os
from requests_html import HTMLSession

def find_passage(filename, book, chapter, start_verse, end_verse):
    try:
        with open(filename, 'r') as file:
            found = False
            result = []
            for line in file:
                columns = line.strip().split('\t')
                if len(columns) >= 6:
                    if columns[0] == book and columns[3] == chapter:
                        if columns[4] == start_verse:
                            found = True
                        elif columns[4] == end_verse:
                            result.append(columns[5])
                            break
                        elif found:
                            result.append(columns[5])
            return "\n".join(result) if result else "Text not found."
    except FileNotFoundError:
        return "File not found."

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

for citation in passages:
    print(citation,"\n")
    book = citation.split(' ', 1)[0]
    chapterverse = citation.split(' ', 1)[1]
    chapter = chapterverse.split(':')[0]
    verse = chapterverse.split(':')[1]
    versesplit_a = verse.split('-')[0]
    versesplit_b = verse.split('-')[1]
    filename = 'bible.txt'
    result = find_passage(filename, book, chapter, versesplit_a,versesplit_b)
    print(result,"\n")

input("Press any key to exit...")

