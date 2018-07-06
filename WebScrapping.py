import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

response = requests.get("https://gaana.com/artist/arijit-singh")
soup = BeautifulSoup(response.text,"html.parser")
print("=============================")
print("Song title",soup.title.text)
print(soup.prettify())
print("=============================")
mTags = soup.find_all('span', class_="parentnode sourcelist_52767")
print("****************")
list1 = []
list2 = []
#for tag in tdTags:
#    #print(tag.text)
#

#mTags = soup.find_all('li', class_="s_duration")
#print("****************")
for tags in mTags:
    #print(tags.text)
    result = re.findall(r"\w+", tags.text)
    print(result)
    y = result.index('title')
    x = result.index('id')
    u = result[y + 1:x]
    title = ' '.join(u)
    list1.append(title)
    # print('-----------')
    z = result.index('duration')
    dur = result[z+1]
    s = int(dur)
    list2.append(s)
    print(title)
    print(dur)
dataset = list(zip(list1,list2))
df = pd.DataFrame(data=dataset,columns=["list1","list2"])
df.to_csv("abc.csv",index=False,header=True)
print(list1)
print(list2)

plt.bar(list1, list2, label="Duration", width=0.5)

plt.legend()

plt.xlabel("Title")
plt.ylabel("Duration")
plt.title("Compare")
plt.show()