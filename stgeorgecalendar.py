import requests
import icalendar
import os
from requests_html import HTMLSession
from icalendar import Calendar, Event


url = "https://stgeorgeroc.org/category/schedules/"

try:
    session = HTMLSession()
    response = session.get(url)
    
except requests.exceptions.RequestException as e:
    print(e)

church_calendar = response.html.find('.entry-content',first=True).text
church_calendar = church_calendar.splitlines()
os.system('cls||clear')

#test

#Father Daniel uses different date formats- just anticipate that.
months = ['Jan','Jan.','January','Feb','Feb.','February','Mar','Mar.','March','Apr','Apr.','April','May.','May','Jun','Jun.','June','Jul','Jul.','July','Aug.','August','Aug.','Sep','Sept','Sep.','Sept.','September','Oct','Oct.','October','Nov','Nov.','November','Dec','Dec.','December']
dates = []

#print(church_calendar)

for item in church_calendar:
    try:
        month = item.split(' ', 1)[1]
        month = month.split(' ', 1)[0]

        if month not in months:
            pass
        else:
            month = month.strip(".")
            day = item.split()[2]
            description = item.split()[3]
            if "Confession" in description:
                description = "Vigil"
            elif "Moleben" in description: 
                description = "Moleben for the sick"
            elif "Vacation" in description:
                description = "Vacation Church School"
            elif "Brotherhood" in description:
                description = "Brotherhood Meeting"
            else:
                description = "Divine Liturgy"
            ampm_time = item.split()[-1]
            time_time = item.split()[-2]
            if time_time[0].isdigit():
                time = time_time+" "+ ampm_time
            else:
                ampm_time = item.split()[-2]
                time_time = item.split()[-3]
                if time_time[0].isdigit():
                    ampm_time = item.split()[-3]
                    time_time = item.split()[-4]
                    time = time_time+" "+ ampm_time
                else:
                    pass

            dates.append([month,day,description,time])
    except:
        pass

print(dates)
print(len(dates), "calendar dates loaded from the St. George Website.")


