# lista original 
lista_original = ['banana', 'pera', 'morango', 'uva', 'laranja']

# ------ Cópia de lista ------

# Forma 1: Usando o método copy()
# Isso cria uma nova lista independente da original
lista_copia = lista_original.copy()
print(f'Lista copiada com copy(): {lista_copia}')

# Forma 2: usando fatiamento [:]
# Esta é outra forma de criar um cópia completa da lista
lista_copia_fatiando = lista_original[:]
print(f'Lista Copiada com fatiamento [:]: {lista_copia_fatiando} ')

# Modificando a copia para provar que a original não muda
lista_copia.append('abacaxi')
print(f'\nLista copia modificada: {lista_copia}')
print(f'Lista original (não mudou): {lista_original}')

# ------------ Fatiamento (slicing) de Letras -------------

# Fatiar é pegar 'pedaços' da lista. A sintaxe é [inicio:fim:passo]

# Pegando os 3 primeiros elementos (do índice 0 até 2)
primeiros_elementos = lista_original[0:3]
print(f'\nFatiamento - 3 primeiros elementos: {primeiros_elementos}')

# Pegando os elementos do índice 2 até o final
do_meio_pra_frente = lista_original[2:]
print(f'\nElementos do indice 2 até o fim: {do_meio_pra_frente}')

# Pegando os últimos 2 elementos
ultimos_elementos = lista_original[-2:]
print(f'Fatiando - Ultimos 2 elementos: {ultimos_elementos}')

# Invertendo a lista com fatiamento
lista_invertida = lista_original[::-1]
print(f"Fatiamento - Lista invertida: {lista_invertida}")