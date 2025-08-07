# verifica_senha_com_tentativas.py

# Exercicio: Verificação de senha com limite de tentativas
senha = input('Digite a senha:')
tent=1

while senha != '1234567AA' and tent<5:
    senha = input('Errado. Digite de novo: ') 
    tent+=1

if senha == "1234567AA":
    print('Senha correta. Tentativas: ',tent)
else:
    print('Tentativas excedidas.')