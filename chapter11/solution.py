import re
fhandle=open("sample.txt",'r')
string = fhandle.read()
lst = re.findall('[0-9]+', string)
sum=None
for n in lst:
    if sum is None:
        sum = int(n)
    else:
        sum = sum + int(n)
print sum
