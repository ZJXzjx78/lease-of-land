import re 
s = 'life is short, i use python,i love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(0,1,2))
print(r.groups())
# r1 = re.findall('life(.*)python',s)
# print(r1)

# r2 = re.match('life(.*)python',s)
# print(r2)
