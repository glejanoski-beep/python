vetor = []

for i in range(8):
    num = int(input('Digite o próximo valor: '))
    vetor.append(num)

for i in range(len(vetor)):
    print(i, end=' ')

print(f'\n{vetor}')

print("Aperte 'Enter' para fechar...")
