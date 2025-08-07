# condicionais/calculo_imc.py

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO NORMAL')
elif 25 <= imc <= 30:
    print('ACIMA DO PESO')
else:
    print('OBESIDADE MÓRBIDA')