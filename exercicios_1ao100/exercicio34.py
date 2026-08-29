mes = int(input("Digite um valor de 1 a 12: "))
ano = int(input("Digite um ano: "))


if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        print("31 dias")
    elif mes == 2:
        print("29 dias")
    elif mes in (4, 6, 9, 11):
        print("30 dias")
    else:
        print("Mês inválido")
else:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        print("31 dias")
    elif mes == 2:
        print("28 dias")
    elif mes in (4, 6, 9, 11):
        print("30 dias")
    else:
        print("Mês inválido")


'''
TESTE 1 
Digite um valor de 1 a 12: 2
Digite um ano: 2024
29 dias

TESTE 2
Digite um valor de 1 a 12: 2
Digite um ano: 2023
28 dias

TESTE 3 
Digite um valor de 1 a 12: 4
Digite um ano: 2026
30 dias

TESTE 4
Digite um valor de 1 a 12: 12
Digite um ano: 2026
31 dias

TESTE 5
Digite um valor de 1 a 12: 13
Digite um ano: 2026
Mês inválido
'''