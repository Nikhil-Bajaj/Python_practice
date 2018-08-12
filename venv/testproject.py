import requests
from bs4 import BeautifulSoup
import html5lib
import requests

import os
def make_soup(URL):
    r = requests.get(URL)
    soupdata = BeautifulSoup(r.content, 'html.parser')
    return soupdata

playerdata=playerdatasaved=""
soup = make_soup("http://howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country=IND")
#x=[]
for record in soup.findAll('tr'):
    #print(record.text)

    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    for data in record.findAll('td'):

        #print(data.text)
        playerdata = playerdata +","+data.text
        print(playerdata)
#    if len(playerdata)!=0:
#    playerdatasaved = playerdatasaved + playerdata[1:]
header = "Name,	TM,	TRuns,	TBatAvg,	TWkts,	TBowlAvg,	OM,	ORuns,	OBatAvg,OWkts,OBowlAvg,T2M,	T2Runs,T2BatAvg,T2Wkts,T2Bowl Avg"
file = open(os.path.expanduser("INDIA PLAYERS.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors="ignore"))

file.write(bytes(playerdata,encoding="ascii",errors="ignore"))
#print(playerdatasaved)

'''


import csv
page = requests.get('http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country=IND')
soup = BeautifulSoup(page.text, 'html.parser')
print("News Source",soup.title.text)

table = soup.find_all('table', class_="TableLined")
"""
with open('indianplayers.csv', 'w+') as csvfile:
    header = "Name,	TM,	TRuns,	TBatAvg,	TWkts,	TBowlAvg,	OM,	ORuns,	OBatAvg,OWkts,OBowlAvg,T2M,	T2Runs,T2BatAvg,T2Wkts,T2Bowl Avg"
    csvfile.write(header)
    spamwriter = csv.writer(csvfile, delimiter=',')  # Changed the delimiter (Way of separating )
    # This opens the CSV file and we set some additional parameters
    for row in soup.find_all('tr'):
        list_of_cell = []
        for cell in soup.find_all('td'):
            text=cell.text
            list_of_cell.append(text)
        print(list_of_cell)
        spamwriter.writerow(list_of_cell)
    #print(tag.text)


list_of_cell = []
with open('indianplayers.csv', 'w+') as csvfile:
    header = "Name,	TM,	TRuns,	TBatAvg,	TWkts,	TBowlAvg,	OM,	ORuns,	OBatAvg,OWkts,OBowlAvg,T2M,	T2Runs,T2BatAvg,T2Wkts,T2Bowl Avg"
    csvfile.write(header)

    for tag in table:

        list_of_cell.append(tag.text.strip())
        print(list_of_cell)
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(list_of_cell)
"""

with open("indianplayers.csv", "a",newline='') as f:
    writeFile = csv.writer(f,delimiter=',')
    for tag in table:
        tdTags = tag.find("td")
        tdTags_string = tdTags.get_text(strip=True)
        writeFile.writerow([tdTags_string])
        #print(tag.text)




"""
rows = soup.find_all('tr')[2]
for tr in rows:
			td = soup.find('td')
			print("%s,%s,%s\n"/
                  (td[0].text,td[1].text,td[2].text))


for tag in tableTags:
    tdTags = soup.find_all('td', class_="TableHeadingRight")
    for tag in tdTags:
        print(tag.text)
        print("@@@@@@@@@@@@@@@@@@@@@@@222")
"""
'''
