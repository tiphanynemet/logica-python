aluno=[]
aluno.append(input("Digite o nome do aluno: "))
aluno.append(input("Digite o RA do aluno: "))
aluno.append(float(input("Digite a NP1: ")))
aluno.append(float(input("Digite a NP2: ")))
media=(aluno[2]+aluno[3])/2
if media >= 7:
    aluno.append("NC")
    aluno.append(media)
    aluno.append(media)
else:
    aluno.append(float(input("Digite o exame do aluno: ")))
    aluno.append(media)
    aluno.append(media+aluno[4])/2

print(aluno)