import re

a = "testтест"

if re.search(r'[^a-zA-Zа-яА-Я]',a ):
     print("error")
else:
     print("ok")