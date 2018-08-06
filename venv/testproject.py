import pandas as pd
import requests
url = "http://howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country=IND"
response = requests.get(url)
#print(response.text)

data = pd.read_html(url)
print(data)