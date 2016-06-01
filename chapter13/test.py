import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL-')

urlh = urllib.urlopen(url)
data = urlh.read()
print data
#tree = ET.fromstring(data)

'''
results = tree.findall('.//count')
sum = None
for count in results:
    if sum is None:
        sum = int(count.text)
    else:
        sum = sum + int(count.text)
print sum
'''
