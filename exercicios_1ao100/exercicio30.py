imovel = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o salário: "))
prazo = int(input("Digite o prazo: "))

prestacao = imovel / (prazo * 12)
limite = salario * 0.3

print(f"Valor do imóve: {imovel}")
print(f"Salário: {salario}")
print(f"Prazo: {prazo}\n")
print(f"Prestação: {round(prestacao, 2)}")
print(f"Limite: {limite}")
if prestacao <= limite: 
    print(f"Aprovado") 
else:
    print(f"Negado")


'''
TESTE 1 
Valor do imóve: 120000.0
Salário: 2000.0
Prazo: 20

Prestação: 500.0
Limite: 600.0
Aprovado

TESTE 2
Valor do imóve: 300000.0
Salário: 3000.0
Prazo: 15

Prestação: 1666.67
Limite: 900.0
Negado

TESTE 3
Valor do imóve: 216000.0
Salário: 2000.0
Prazo: 30

Prestação: 600.0
Limite: 600.0
Aprovado

'''