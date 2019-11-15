import re
a = 'abc,acc,adc,afc,ahc'
r = re.findall('a[cf]c',a)
print(r)