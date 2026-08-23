A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

print(f"\nA: {A}")
print(f"B: {B}")

aux = A
A = B
B = aux

print(f"\nDepois da troca: ")
print(f"A: {A}")
print(f"B: {B}")

# Inclusão para validação final

aux = B
B = A
A = aux
print(f"\nSegunda da troca: ")
print(f"A: {A}")
print(f"B: {B}")

'''
TESTE 1

Digite o valor de A: 10
Digite o valor de B: 50
A: 50
B: 10

TESTE 2 

A: 5
B: 1

Depois da troca: 
A: 1
B: 5


TESTE 3

A: 1
B: 2

Depois da troca: 
A: 2
B: 1

Segunda da troca: 
A: 1
B: 2



'''

