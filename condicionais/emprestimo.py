# condicionais/emprestimo.py

salario_bruto = float(input('Digite o salário bruto: '))
numero_parcelas = int(input('Número de parcelas: '))
valor_prestacao = float(input('Valor da prestação: '))

valor_max = salario_bruto * 0.30

if valor_prestacao <= valor_max:
    print('O empréstimo pode ser concedido')
else:
    print('O empréstimo não pode ser concedido')