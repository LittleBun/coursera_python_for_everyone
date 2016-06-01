import urllib
import json

url = raw_input('Enter URL- ')
urlh = urllib.urlopen(url)
string = urlh.read()

info = json.loads(string)
sum = None
for w in info["comments"]:
    if sum is None:
        sum = int(w["count"])
    else:
        sum = sum + int(w["count"])
print sum
