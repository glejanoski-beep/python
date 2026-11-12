qtde = 0
media = 0.0
soma = 0
maiores = 0

while True:
    idade = int(input('Digite uma idade: '))

    if idade < 0:
        print('Encerrado!')
        break
    else:
        qtde += 1
        soma += idade
        if idade >= 18:
            maiores += 1



if qtde == 0:
    print('Nenhuma idade informada')
else:
    media = soma / qtde
    print(f'Quantidade: {qtde}')
    print(f'Média: {media}')
    print(f'Maiores de 18 anos: {maiores}')
    print("Aperte 'Enter' para fechar...")