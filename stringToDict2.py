#!/usr/bin/python3
print("Content-type: text/html;charset=iso-8859-1 \n\n")

print("<style>BODY { font-family: Heebo;}</STYLE>")
# http://localhost/Python/stringToDict.py
#dictdump = { "test1":"1", "test2":123, "test3":345  }
print('<h1>DICTs & JSON (Multidimensional)</h1>')

import json
with open("C:\\Inetpub\\wwwroot\\Python\\dump.txt", encoding="utf-8") as handle:
    dictdump = json.loads(handle.read())

print(f"dictdump é dict ? {isinstance(dictdump,dict)}<br>")
print(f'Dictdump: {dictdump} <br>')
#print(type(dictdump))
print(f"dictdump['test4']: {dictdump['test4']}<br>")
print(f'dictdump["itens"]: {dictdump["itens"]}<br>')
print(f"dictdump['itens']['sim']: {dictdump['itens']['sim']}<br>")
print("---------------------------------------------<br>")
print(f"dictdump['veiculos']['0']: {dictdump['veiculos']['0']}<br>")
print(f"dictdump['veiculos']['0']['marca']: {dictdump['veiculos']['0']['marca']}<br>")

str1 = json.dumps(dictdump)
print(f"dictdump é string ? {isinstance(str1,str)}<br>")