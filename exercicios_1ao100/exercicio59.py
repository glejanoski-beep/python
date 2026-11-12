senha = 1234
tentativas = 0

while True:
    s = int(input("Digite a senha para liberar o acesso: "))

    if s == senha:
        print('Acesso liberado')
        tentativas += 1
        break
    else:
        print('Senha incorreta! Tente novamente')
        tentativas += 1

print(f'Tentativas: {tentativas}')
print("Aperte 'Enter' para fechar...")