# Listas dentro de listas ( listas aninhadas / matriz)

print('='*55)
print('Listas dentro de listas ( listas aninhadas / matriz)')
print('='*55 + '\n')

# 1 - Exemplo basico: criando uma lista dentro de lista

# Matriz simples
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('Matriz original:')
print(matriz)
print(f'Tipo: {type(matriz)}')
print(f'Quantidade de linhas: {len(matriz)}')
print(f'Quantidade de colunas (primeira linha): {len(matriz[0])}')

print('='*55 + '\n')

# 2 - Acessando elementos da lista aninhada
print('Acessando elementos da lista aninhada')
print('='*55 + '\n')

print('Acessando elementos individuais')
print(f'Matriz[0]: {matriz[0]} (primeira linha)')
print(f'Matriz[1]: {matriz[1]} (segunda linha)')
print(f'Matriz[2]: {matriz[2]} (terceira linha)\n')

print('Acessando elementos especificos:')
print(f'Matriz[0][0]: {matriz[0][0]} (linha 0 - coluna 0)')
print(f'Matriz[0][1]: {matriz[0][1]} (linha 0 - coluna 1)')
print(f'Matriz[1][1]: {matriz[1][1]} (linha 1 - coluna 1)')
print(f'Matriz[2][2]: {matriz[2][2]} (linha 2 - coluna 2)')
print("="*55 + "\n")

# 3 - Modificando em listas aninhadas

print('Modificando elementos')
print("="*55 + "\n")

matriz_modificada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('Matriz Original:')
for linha in matriz_modificada:
    print(linha)

print('\nModificando matriz [1][1] de 5 para 99')
matriz_modificada[1][1] = 99

print('Matriz Modificada:')
for linha in matriz_modificada:
    print(linha)

print('\nModificando matriz[2][0] de 7 para 77')
matriz_modificada[2][0] = 77

print('Matriz Modificada:')
for linha in matriz_modificada:
    print(linha)

print("\n" + "="*60 + "\n")


# 4 - Iterando sobre linhas aninhadas

print('Iterando sobre linhas aninhadas')
print("="*60 + "\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('Usando "for" simples')

for linha in matriz:
    print(linha)

print('\nUsando for aninhado (acessar cada elemento):')
for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        print(f'matriz[{i}][{j}]: {elemento}', end=' ')
    print()