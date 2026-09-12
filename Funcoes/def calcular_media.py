def calcular_media(lista_numeros):
    total = sum(lista_numeros)
    quantidade = len(lista_numeros)

    if  quantidade == 0:
        return 0
    media = total / quantidade
    return media

notas_alunos1 = [8.5, 7.0, 9.0, 10.0]

print(calcular_media(notas_alunos1))