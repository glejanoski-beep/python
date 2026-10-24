pares = 0
impares = 0

for i in range(6):
    i = int(input(('Digite um valor:')))

    if i % 2 == 0:
        pares+=1
    else:
        impares+=1

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
print("Aperte 'Enter' para fechar...")