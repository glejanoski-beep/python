vetor = []
valor = 0

for i in range(10):
    valor = 5 * (i + 1)
    vetor.append(valor)


for i in range(len(vetor)):
    print(i, end=' ')
print(f'\n{vetor}')
print("Aperte 'Enter' para fechar...")