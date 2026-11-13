vetor = []
vetor_reverso = []

for i in range(3):
    num = int(input('Digite o próximo valor: '))
    vetor.append(num)


vetor_reverso = vetor[::-1]
print(vetor_reverso)  
vetor_reverso.clear()

for i in range(len(vetor) - 1, - 1, -1):
    vetor_reverso.append(vetor[i])


print(vetor)
print(vetor_reverso)   

print("Aperte 'Enter' para fechar...")