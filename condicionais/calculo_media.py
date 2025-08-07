# condicional/media_aluno.py

aluno = input("Digite o nome: ")
np1 = float(input("Nota 1: "))
np2 = float(input("Nota 2: "))
mediaS = (np1 + np2) / 2

if mediaS >= 7:
    print(f"\nO aluno {aluno} foi aprovado com média igual a {mediaS:.2f}")
else:
    nota_exame = 10 - mediaS
    print(f"\nO aluno(a) {aluno} ficou com média inferior a 7. Precisará tirar {nota_exame:.2f} no exame.")

