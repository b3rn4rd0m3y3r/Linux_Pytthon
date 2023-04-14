#!/usr/bin/python3
print("Content-Type: text/html; charset=utf-8\n\n")
print("<h1>Leitura de arquivos</h1>")
f = open("./Dados/exfile2.txt", "r")
for line in f:
    print(line, end='<br>')
