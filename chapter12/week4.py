import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
total = None
for tag in tags:
    if total == None:
        total=int(tag.contents[0])
    else:
        total = total + int(tag.contents[0])
print total
