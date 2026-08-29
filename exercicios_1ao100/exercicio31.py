num = int(input("Digite um valor: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"O numero {num}  É divisível por 3 e 5")
elif num % 3 == 0 and num % 5 != 0:
    print(f"O numero {num} É  disivível apenas por 3")
elif num % 3 != 0 and num % 5 == 0:
    print(f"O numero {num} É  disivível apenas por 5")
else:
    print(f"O numero {num} NÃO É disivível apenas por 3 NEM por 5")

'''
TESTE 1 
O numero 30  É divisível por 3 e 5

TESTE 2
O numero 9 É  disivível apenas por 3

TESTE 3 
O numero 20 É  disivível apenas por 5

TESTE 4
O numero 7 NÃO É disivível apenas por 3 NEM por 5

'''