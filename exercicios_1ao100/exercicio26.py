salario = float(input("Digite o salário: "))

ajuste1 = salario * 0.15
ajuste2 = salario * 0.1
ajuste3 = salario * 0.05 

if salario <= 1500:
    print(f"Ajuste de 15%. Adicional de {ajuste1}. Novo Salário: {salario + ajuste1}")
elif salario > 1500 and salario < 3000:
    print(f"Ajuste de 10%. Adicional de {round(ajuste2, 2)}. Novo Salário: {round(salario + ajuste2, 2)}")
else:
    print(f"Ajuste de 5%. Adicional de {round(ajuste3, 2)}. Novo Salário: {round(salario + ajuste3, 2)}")


'''
TESTE 1 
Digite o salário: 1500
Ajuste de 15%. Adicional de 225.0. Novo Salário: 1725.0

TESTE 2 
Digite o salário: 1500.01
Ajuste de 10%. Adicional de 150.0. Novo Salário: 1650.01

TESTE 3 
Digite o salário: 4000
Ajuste de 5%. Adicional de 200.0. Novo Salário: 4200.0

'''

