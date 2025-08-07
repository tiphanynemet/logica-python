# listas/forma_pagamento.py

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3]
print("Maior: ", max(lista))
print("Menor: ", min(lista))
print("Pares: ", end=" ")
media = 0
somaneg = 0
for i in lista:
    if i % 2 == 0:
        print(i, end=" ")
    media += i
    if i < 0:
        somaneg += i
print("\n{0} ocorre {1} vezes".format(lista[0], lista.count(lista[0])))
print("Média: ", media / len(lista))
print("Soma dos negativos: ", somaneg)