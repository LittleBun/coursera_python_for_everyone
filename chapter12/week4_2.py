import urllib
from BeautifulSoup import *

url = raw_input('Enter URL- ')
count = int(raw_input('Enter count- '))
pos = int(raw_input('Enter position- '))
for i in range(count):
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html)

    tags = soup('a')
    name=tags[pos-1].contents[0]
    print name
    url = tags[pos-1].get('href', None)

