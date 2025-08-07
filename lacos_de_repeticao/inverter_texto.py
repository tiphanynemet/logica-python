# inverter_texto.py

# Exercício: Imprimir o texto digitado ao contrário usando while

texto = input('Digite um texto: ')
indice = len(texto) - 1

while indice >= 0:
    print(texto[indice], end="")
    indice -= 1