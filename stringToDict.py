#!/usr/bin/python3
print("Content-type: text/html \n\n")
print("<style>BODY { font-family: Heebo;}</STYLE>")
# http://localhost/Python/stringToDict.py
#dictdump = { "test1":"1", "test2":123, "test3":345  }
print('<h1>DICTs & JSON (variável/arquivo)</h1>')

import json
with open("C:\\Inetpub\\wwwroot\\Python\\dump.txt") as handle:
    dictdump = json.loads(handle.read())

print(f"dictdump é dict ? {isinstance(dictdump,dict)}<br>")
print(f"Dictdump: {dictdump} <br>")
#print(type(dictdump))
print(f"dictdump['test4']: {dictdump['test4']}<br>")

str1 = json.dumps(dictdump)
print(f"dictdump é string ? {isinstance(str1,str)}<br>")