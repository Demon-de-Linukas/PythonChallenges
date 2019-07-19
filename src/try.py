import re

sth='and the next nothing is 80119'
print(re.findall(r'next nothing.*',sth))