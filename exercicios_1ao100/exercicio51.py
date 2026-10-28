menor: int
maior: int
numeros =[]

for i in range(10):
    valor = int(input('Digite um valor:'))
    numeros.append(valor)

    if i == 0:
        menor = maior = valor
    else:
        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor


print(f'Números digitados: {numeros}')
print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
print("Aperte 'Enter' para fechar...")