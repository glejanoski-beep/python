alturas = []
media = 0.0

for i in range(3):
    altura = float(input('Digite uma altura:'))
    alturas.append(altura)
    media += altura

menor = min(alturas)
maior = max(alturas)

print(f'As alturas informadas: {alturas}')
print(f'Menor altura: {menor} m')
print(f'Maior algura: {maior} m ')
print(f'Média das alturas: {media/len(alturas):.2f} m')
print("Aperte 'Enter' para fechar...")


