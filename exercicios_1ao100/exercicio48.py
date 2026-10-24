positivos = []
negativos = []
zero = []

for i in range(8):
    valor = int(input('Digite um número inteiro:'))

    if valor < 0:
        negativos.append(valor)
    elif valor > 0:
        positivos.append(valor)
    else:
        zero.append(valor)

print(f'Positivos: {len(positivos)}')
print(f'Negativos: {len(negativos)}')
print(f'Zeros: {len(zero)}')

print("Aperte 'Enter' para fechar...")