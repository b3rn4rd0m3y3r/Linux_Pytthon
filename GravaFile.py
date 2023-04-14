#!/usr/bin/python3
print("Content-type: text/html;charset=utf-8 \n\n")
print('<h1>Gravação em arquivo</h1>')
f = open("./Dados/exfile3.txt", "a")
for i in range(1,100):
    f.write("Linha " + str(i) + " para arquivo\n")
    print(f'{i} ')
f.close()
