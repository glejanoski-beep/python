preco = float(input("Digite o valor do produto: "))

desconto = preco * 0.1
precofinal = round(preco - desconto, 2)

print(f"Preço: {preco}\n")

# Inclusão do :.2f após identificar 3 casas decimais nas respostas
print(f"Desconto: {desconto:.2f}")
print(f"Preço Final: {preco - desconto}")

# Incluí após verificar que tinha mais casas decimais do que o solicitado 
print(f"Preço Final (com round): {precofinal}")

'''
TESTE 1

Preço: 50.0

Desconto: 5.0
Preço Final: 45.0

TESTE 2

Preço: 73.99

Desconto: 7.40
Preço Final: 66.591
Preço Final: 66.59

TESTE 3

Preço: 99.9

Desconto: 9.99
Preço Final: 89.91
Preço Final: 89.91


'''