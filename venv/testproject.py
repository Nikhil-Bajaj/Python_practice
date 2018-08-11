import requests
from bs4 import BeautifulSoup
import html5lib
import requests
from bs4 import BeautifulSoup
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
    playerdata=""
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    for data in record.findAll('td'):

        #print(data.text)
        playerdata = playerdata +","+data.text
        if len(playerdata)!=0:
            playerdatasaved = playerdatasaved + playerdata[1:]
header = "Name,	TM,	TRuns,	TBatAvg,	TWkts,	TBowlAvg,	OM,	ORuns,	OBatAvg,OWkts,OBowlAvg,T2M,	T2Runs,T2BatAvg,T2Wkts,T2Bowl Avg"
file = open(os.path.expanduser("INDIA PLAYERS.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors="ignore"))

file.write(bytes(playerdatasaved,encoding="ascii",errors="ignore"))
#print(playerdatasaved)

