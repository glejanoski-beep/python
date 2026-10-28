idade: int
todas_idades = []
media = maiores = menores = 0

for i in range(10):
    idade = int(input('Digite uma idade:'))
    todas_idades.append(idade)
    media += idade

    if idade < 18:
        menores += 1

    if idade >= 60:
        maiores += 1

print(f'Média das idades é {(media/len(todas_idades))}')
print(f'Menores de 18: {menores}')
print(f'Maiores de 60: {maiores}')
print("Aperte 'Enter' para fechar...")
