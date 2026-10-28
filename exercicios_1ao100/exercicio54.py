valor_A = int(input('Digite o valor A: '))
valor_B = int(input('Digite o valor B: '))
total_B = total_A = 0

for i in range(valor_A):
    if i % 3 == 0:
        total_A+=i

for j in range(valor_B):
    if j % 3 == 0:
        total_B +=j

print(f'Somas dos múltiplos de 3: {(total_A + total_B)}')
    

