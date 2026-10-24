listaNotas = []
media = 0
nota = 0

while len(listaNotas) < 10:
    nota = int(input('Digite uma nota entre 0 e 10:'))

    if nota < 0 or nota > 10:
        print('Valor inválido')
    else:
        listaNotas.append(nota)

for j in range(len(listaNotas)):
        media += listaNotas[j]
    
media = media / len(listaNotas)
print(f'{media:.2f}')
print("Aperte 'Enter' para fechar...")