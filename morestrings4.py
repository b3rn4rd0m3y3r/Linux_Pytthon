#!/usr/bin/python3
print('Content-type: text/html;charset=utf-8 \n\n')
print('<h1>strings PYTHON 3</h1>')

Registro = "001;Aurélio de Souza;Rua Andradina 67;Canoas;Florianopolis;SC"
Arr = Registro.split(';')
print(f"Nome { Arr[1] } <br>")
print(f"Endereço { Arr[2] } <br>")

