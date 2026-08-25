valor_unit = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
frete = float(input("Digite o valor do frete: "))

subtotal = valor_unit * quantidade
total = subtotal + frete

print(f"Preço unitário: R${valor_unit}")
print(f"Quantidade: {quantidade}")
print(f"Frete: R${frete}\n")
print(f"Subtotal: R${subtotal}")
print(f"Total: R${total}")


# VALIDAÇÃO FINAL 

print(f"validação: R${total - subtotal}")

'''
TESTE 1 
Preço unitário: R$10.0
Quantidade: 3
Frete: R$5.0

Subtotal: R$30.0
Total: R$35.0

TESTE 2

Preço unitário: R$12.99
Quantidade: 5
Frete: R$10.8

Subtotal: R$64.95
Total: R$75.75

TESTE 3 

Preço unitário: R$7.5
Quantidade: 10
Frete: R$12.0

Subtotal: R$75.0
Total: R$87.0
validação: R$12.0



'''