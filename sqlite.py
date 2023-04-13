#!/usr/bin/python3
print("Content-type: text/html \n\n")
print('<h1>Sqlite</h1>')

import sqlite3
conn = sqlite3.connect('./Banco.db')
print("Opened database successfully")
cur = conn.cursor()
print("<table>")
for row in cur.execute("SELECT * FROM Teste"):
    tId = row[0]
    tDescri = row[1]
    print(f'<tr><td>{tId}</td><td>{tDescri}</td></tr>')
print("</table>")
