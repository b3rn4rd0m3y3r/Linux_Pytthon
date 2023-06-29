#!/usr/bin/python3
print("Content-type: text/html \n\n")
print('<h1>Sqlite</h1>')

import sqlite3
conn = ""
rs = ""

conn = sqlite3.connect('C:\\Inetpub\\wwwroot\\Python\\Banco.db')

cur = conn.cursor()
try:
	rs = cur.execute("SELECT * FROM Teste")
	print("Opened recordset successfully")
except Exception as e:
	print('Tabela não existe. Exception: {}'.format(e))

print("<table>")
for row in rs:
    tId = row[0]
    tDescri = row[1]
    print(f'<tr><td>{tId}</td><td>{tDescri}</td></tr>')
print("</table>")
