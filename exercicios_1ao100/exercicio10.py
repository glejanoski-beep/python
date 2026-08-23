salario_base = float(input("Digite o salário fixo: "))
total_vendido = float(input("Digite o total vendido: "))

comissao = total_vendido * 0.04

print(f"Salário fixo: R${salario_base}")
print(f"Total vendido: R${total_vendido}\n")
print(f"Comissão: {comissao:.2f}")
print(f"Salário Total: {round(salario_base + comissao, 2)}")

'''
TESTE 1

Salário fixo: R$2500.0
Total vendido: R$20000.0

Comissão: 800.00
Salário Total: 3300.0

TESTE 2

Salário fixo: R$3000.0
Total vendido: R$0.0

Comissão: 0.00
Salário Total: 3000.0

TESTE 3

Salário fixo: R$1200.0
Total vendido: R$23575.5

Comissão: 943.02
Salário Total: 2143.02

'''

