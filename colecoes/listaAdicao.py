# Adição de Elementos em lista
frutas = ['pera', 'banana', 'laranja']
print(f'Lista original: {frutas}\n')

# 1 - Usando 'append' - adionando um elemento no final da lista
frutas.append('morango')
print(f'Apos append - morango: {frutas}')

frutas.append('uva')
print(f'Apos append - uva: {frutas}')

print('\n' + '_'*50 + '\n')

# 2 - Usando 'extend' - adiciona multiplos elementos no final
numeros = [1, 2, 3]
print(f'Lista numeros original: {numeros}')

numeros.extend([4, 5, 6])
print(f'\nApos exetend - 4, 5 , 6: {numeros}')

numeros.extend([7, 8])
print(f'Apos extend - 7, 8: {numeros}')

print('\n' + '_'*50 + '\n')

# 3 - Usando 'insert' - adiciona um elemento em uma posição específica 
cores = ['vermelho', 'azul', 'verde']
print(f'Lista cores original: {cores}\n')

cores.insert(1, 'amarelo')
print(f'Apos insert (1, amarelo): {cores}\n')

cores.insert(0, 'roxo')
print(f'Apos insert (0, roxo): {cores}\n')

cores.insert(len(cores), 'preto')
print(f'Apos insert (len(cores, preto)): {cores}')

print('\n' + '_'*50 + '\n')

# 4 - usando + (concatenação) - cria uma nova lista
lista1 = [1, 2 , 3]
lista2 = [4, 5 , 6]
print(f'Lista1', lista1)
print('Lista2', lista2)

lista3 = lista1 + lista2
print('Lista3', lista3)
print(f'Lista1: {lista1} \nLista2: {lista2}', )







      
