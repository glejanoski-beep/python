


soma= 0 
quantidade = 0
media = 0.0


while True:
    valor = int(input('Digite um valor. Se for zero, encerra o programa: '))

    if valor == 0:
        break
    else:
        soma += valor
        quantidade += 1
        media = soma / quantidade

if quantidade == 0:
        print('Nenhum valor válido!')
else:
    print(f'Soma: {soma}')
    print(f'Quantiadade: {quantidade}')
    print(f'Média: {media}')


print("Aperte 'Enter' para fechar...")