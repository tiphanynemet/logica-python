# tabuada_while.py

# Exercício: Tabuada do número fornecido usando laço while

numero = int(input("Tabuada do número: "))
contador = 0

while contador <= 10:
    resultado = numero * contador
    print(f'{contador} x {numero} = {resultado}')
    contador += 1

