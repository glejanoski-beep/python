salario = float(input("Digite o salário atual: "))

aumento = salario * 0.15

# Inclusão para validação final
novo_salario = salario + aumento

print(f"Salário atual: {salario}\n")
print(f"Aumento: {aumento}")
print(f"Novo salário: {round(salario + aumento, 2)}")

# Inclusão para validação final
print(f"Validação: {round(novo_salario - salario, 2)}")

'''
TESTE 1

Salário atual: 1200.0

Aumento: 180.0
Novo salário: 1380.0

TESTE 2

Salário atual: 2200.0

Aumento: 330.0
Novo salário: 2530.0

TESTE 3

Digite o salário atual: 3500
Salário atual: 3500.0

Aumento: 525.0
Novo salário: 4025.0
Validação: 525.0

'''