# Lista
frutas = ['morango', 'banana', 'uva', 'laranja']

# Acessando elementos por seu íncide
primeira_fruta = frutas[0]
segunda_fruta = frutas[2]

print(f"Lista completa: {frutas}")
print(f"Primeira fruta: {primeira_fruta}")
print(f"Segunda fruta: {segunda_fruta}")

# Usando índices negativos para começar  o final da lista
ultima_fruta = frutas[-1]
penultima_fruta = frutas[-2]

print(f"Ultima fruta: {ultima_fruta}")
print(f"Penultima fruta: {penultima_fruta}")

# Modificando um elemento da lista usando seu índice
print(f'\nLista antes da modificação: {frutas}')
frutas[1] = 'pera'
print(f'\nLista depois da modificação do indice 1: {frutas}')

# Obtendo o tamanho da lista para saber o último índice válido
tamanho_lista = len(frutas)
print(f"\nA lista tem {tamanho_lista} elementos")
print(f"Os indices validos vao de 0 a {tamanho_lista -1}")