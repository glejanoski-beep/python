# Remoção de elementos em lista

# 1 - Usando remove() - remove a primeira ocorrência de um valor
frutas = ['pera', 'banana', 'laranja', 'banana']
print('Lista Original', frutas)

frutas.remove('banana')
print('\nApos remove banana', frutas)

frutas.remove('pera')
print('\nApos remove pera', frutas)

print('\n' + '-'*50 + '\n')

# 2 - usando pop() - remove elemento por índice e retorna o valor
numeros = [1, 2, 3, 4, 5]
print('Lista original:', numeros)

removido = numeros.pop()    # removendo ultimo elemento
print('\nNumero removido:', removido)
print('\n lista apos pop:', numeros)

removido = numeros.pop(0)   # removendo o primeiro elemento
print('\nNumero removido:', removido)
print('\n lista apos pop:', numeros)

removido = numeros.pop(1)
print('\nNumero removido:', removido)
print('\n lista apos pop:', numeros)

print('\n' + '-'*50 + '\n')

# 3 - usando del - remove elemento por índice
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
print('Lista original:', cores)

del cores[0]
print('\n apos del(0):', cores)

del cores[2]
print('\n apos del(0):', cores)


print('\n' + '-'*50 + '\n')

# 4 - usando del com fatias - remove mútiplos elementos
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('Lista original:', letras)

del letras[1:3]     # removendo elementos do índice 1 ao 2
print('\nApos del com slice:', letras)

print('\n' + '-'*50 + '\n')

# 5 - Usando clear() - remove todos os elementos
animais = ['gato', 'cachorro', 'passaro', 'peixe']
print('lista original:', animais)

animais.clear()
print('\nApos o clear():', animais)

print('\n' + '-'*50 + '\n')

# --------- Exemplos práticos ---------

# Remover último elemento de uma fila
fila = [1, 2 , 3 , 4]
print('Fila:', fila)
print('Removendo ultimo elemento:', fila.pop())
print('Fila atualizada:', fila)
print('\n' + '-'*50 + '\n')

# Remover primeiro elemento da fila
fila2 = ['primeiro', 'segundo', 'terceiro']
print('Fila2:', fila2)
print('Removendo primeiro elemento:', fila2.pop(0))
print('Fila atualizada:', fila2)
print('\n' + '-'*50 + '\n')

# Limpar lista completa
temporaria = [10, 20, 30, 40]
print('Temporaria:', temporaria)
temporaria.clear()
print('Temporaria apos o clear:', temporaria)