preco = float(input("Digite o valor do produto: "))
opcao = int(input("Digite a forma de pagamento desejada:\n 1 - Dinheiro ou Pix\n 2 - Débito\n 3 - Crédito à vista\n 4 - Crédito parcelado\n"))

if opcao == 1:
    print(f"Preço: {preco}\n Opção: {opcao}\n\n Valor Final: {preco - (preco * 0.1)}")
elif opcao == 2:
    print(f"Preço: {preco}\n Opção: {opcao}\n\n Valor Final: {preco - (preco * 0.05)}")
elif opcao == 3:
    print(f"Preço: {preco}\n Opção: {opcao}\n\n Valor Final: {preco}")
else:
    print(f"Preço: {preco}\n Opção: {opcao}\n\n Valor Final: {preco + (preco * 0.08)}")


'''
TESTE 1 
reço: 200.0
 Opção: 1

 Valor Final: 180.0

 TESTE 2
 Preço: 200.0
 Opção: 2

 Valor Final: 190.0

 TESTE 3 
 Preço: 200.0
 Opção: 3

 Valor Final: 200.0

 TEST2 4 
 Preço: 200.0
 Opção: 4

 Valor Final: 216.0

'''