#This Script Collects all News from Google.com/News

import requests
from bs4 import BeautifulSoup

#Get Indian Google news page
print('Connecting to Google News...')
result = requests.get('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en')

#If Connection Success Continue else Stop
if result.status_code == requests.codes.ok:
    print('Connection Succesful!')
    print('Fetching News , Just a Min...')
else:
    raise Exception('Sorry , Unable to Fetch News , Try again after some Time')

#Get Source of Page
src = result.content

#Create Soup Object
soup = BeautifulSoup(src , features="html.parser")

#Store Headlines in a List
headlines = []

#Since All Headlines are stored in h3 tag find all of them
#And Get Links from those h3 tags and add the text of those Links
#To our Headlines List
for h3_tag in soup.find_all('h3'):
    link = h3_tag.find('a')
    headlines.append(link.text)

for i in range(0,len(headlines)):
    print('\t',end='')
    print('{}]'.format(i+1),end=' ')
    print(headlines[i],end='\n')
    print('\n')
