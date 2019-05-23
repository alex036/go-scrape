from bs4 import BeautifulSoup
import requests

page = requests.get("http://gotracker.ca/GoTracker/mobile/StationStatus/Service/01/Station/3")
c = page.content
soup = BeautifulSoup(c,features="html.parser")

title = soup.find("span", {"id" : "lblPageTitle2"})
print(title.text)

body = soup.find("tr", {"class" : "sTbl"})
header = body.find_all("td")
print(header[1].text)

times = body.find_all("tr")

for entry in times[2:]:
    try:
        className = entry.attrs['class'][0]
        #print(className)
        if (className == "oddRowTR") or (className == "topDoubleRowTR"):
            if entry.find("td", {"class" : "colTripExpected"}).text != "On Time":
                delay = " !!!!!"
            else:
                delay = ""
            print(
            "Destination: " + entry.find("td", {"class" : "colTripDestination"}).text +
            " Scheduled: " + entry.find("td", {"class" : "colTripScheduled"}).text +
            " Track: " + entry.find("td", {"class" : "colTripTrack"}).text +
            " Expected: " + entry.find("td", {"class" : "colTripExpected"}).text + delay)
        if className == "directionHeaderTH":
            print(entry.find("td").text)
    except KeyError as e:
        True
