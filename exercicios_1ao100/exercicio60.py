
compra = []

while True:
    valor = float(input('Informe o valor do proximo produto. Para finalizar, digite zero (0): '))

    if valor == 0 or valor == 0.0:
        print('Compra encerrada.')
        break
    else:
        compra.append(valor)



if  not compra:
    print('Nenhum valor informado.')
else:
    quantidade = len(compra)
    total = sum(compra)
    maiorPreco = max(compra)
    
    print(f'Produtos: {quantidade}')
    print(f'Total: {total}')
    print(f'Maior preço: {maiorPreco}')

print("Aperte 'Enter' para fechar...")