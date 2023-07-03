#Parses BBDC booking schedule to save into calendar
import uuid
from bs4 import BeautifulSoup
from datetime import datetime
import sys


with open(sys.argv[1], "r") as f:
    soup = BeautifulSoup(f, "html.parser")

all_schedule = soup.find_all("div", {"class" : "col-sm-4 col-6"})

if len(sys.argv) == 3:
    cal = open(sys.argv[2], "w")

else:
    cal = open("BBDCParsed.ics", "w")

cal.write("BEGIN:VCALENDAR\n")
cal.write("VERSION:2.0\n")
cal.write("PRODID:-//MyCalendar//EN\n")

for i in all_schedule:
    title = i.find(class_="title").get_text().lstrip()
    date = i.find(class_ = "date").get_text()[:10]
    date = date.split("-")
    time = i.find(class_ = "startTime").get_text()[:12].lstrip()
    time = time.split("-")
    start_time = datetime.strptime(time[0],"%H:%M")
    end_time = datetime.strptime(time[1],"%H:%M")
    now = datetime.now().strftime("%Y%m%dT%H%M%S")      
    delta = (end_time - start_time).total_seconds()
    hours = int(delta // 3600)
    minutes = int((delta - hours*3600) / 60)
    if hours == 0 : duration = f'PT{minutes}M'
    elif minutes == 0: duration = f'PT{hours}H'
    else: duration = f'PT{hours}H{minutes}M'
    id = str(uuid.uuid4())
    cal.write("BEGIN:VEVENT\n")
    cal.write("DTSTAMP:" + now + "\n")
    cal.write("SUMMARY:" + title + "\n")
    cal.write("UID:" + id + "\n")
    cal.write("DTSTART:" + date[2] + date[1] + date[0] + "T" + time[0][:2] + time[0][3:] + "00\n")
    cal.write("DURATION:" + duration + "\n")
    cal.write("END:VEVENT\n")

cal.write("END:VCALENDAR")
cal.close()



