# Listas em Python

# Criando uma lista de frutas
frutas = ["morango", "banana", "laranja", "uva"]
print(f"listas de frutas: {frutas}")

# Acessando elementos
primeira_fruta = frutas[0]
print(f"\nprimeira fruta: {primeira_fruta}")

# Modificando elementos
frutas[0] = "pera"
print(f"\nAlterado a grita 'banana' por 'pera' na lista: {frutas}")

# Adicionando elementos
frutas.append("abacaxi")
print(f"\nO 'append' adiciona um valor '{frutas[4]}' no final da lista: {frutas}")

# Fatiando (slicing) a lista de frutas
primeiras_duas = frutas[0:2]
print(f"\nAs duas primeiras frutas da lista: {primeiras_duas}")

# Obtendo o tamanho da lista de frutas
tamanho_frutas = len(frutas)
print(f"\nTamanho da lista de frutas: {tamanho_frutas}")

# Iterando sobre lista de frutas
print("\nIterando sobre a lista de frutas: ")
for fruta in frutas:
    print(fruta)


# -------------------- Lista Numérica -------------------

# Criando uma lista numérica
z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nLista numerica z: {z}")

# Acessando um elemento da lista z
terceiro_elemento = z[2]
print(f"\nO terceiro elemento da lista eh: {terceiro_elemento}")

# Fatiando a lista z
primeiros_cinco = z[0:5]
print(f"\nOs cinco primeiros elementos da lista: {primeiros_cinco}")

# Funções de lista numérica
soma_z = sum(z)
menor_valor_z = min(z)
maior_valor_z = max(z) 



# --- Imprimindo resultados ---
print("\nresultado das funções em lista numericas:")

print(f"\nSoma de todos elementos da lista z: {soma_z}")
print(f"Menor valor da lista z: {menor_valor_z}")
print(f"Maior valor da lista z: {maior_valor_z}")
print(f"Tamanha da lista z: {len(z)}")
print(f"Media dos valores na lista z: {soma_z / len(z)}")
print(f"valores unicos em z: {set(z)}")
print(f"Lista Z ordenada: {sorted(z)}")
print(f"Lista Z em ordem reversa: {list(reversed(z))}")
print(f"Lista z convertida em tupla: {tuple(z)}")
print(f"Lista z convertida em string: {str(z)}")
print(f"Lista z convertida em conjunto: {set(z)}")
print(f"Lista z convertida em dicionario: {dict(enumerate(z))}")

# --- Lista usando list comprehension ---
quadrados = [x**2 for x in z]
print(f"\nLista de quadrados nos elementos em z: {quadrados}")

# Filtrnado elemnetos pares usando list comprehension
pares = [x for x in z if x % 2 == 0]
print(f"lista de numeros pares em z: {pares}")

# mapeando elementos para dobrar seus valores
dobrados = [x * 2 for x in z ]
print(f"lista de elementos de z dobrados: {dobrados}")

# Criando uma lista de tuplas (numero, seu quadrado)
tuplas_quadrados = [(x, x**2) for x in z]
print(f"Lista de tuplas (numero, seu quadrado): {tuplas_quadrados}")

# --- while loop para iterar sobre a lista z
print("\nIterando sobre a lista z usando 'while'.")
i = 0 
while i < len(z):
    print(z[i])
    i += 1

# Usando enumerate para obter índice e valor
print("\nIterando sobre a lista z usando enumerate")
for index, value in enumerate(z):
    print(f"Indice: {index}, Valor: {value}")

# Usando 'zip' para combinar duas listas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
combinado = list(zip(z, letras))
print(f"Lista combinada de z e letras: {combinado}")

# Usando 'map' para aplicar uma função a todos os elementos
# map aplica a função a cada elemento da sequencia
def cubo(x):
    return x**3

cubos = list(map(cubo, z))
print(f'\nLista de cubos dos elementos em z: {cubos}')

# Usando 'filter' para filtrar elementos maiores que 5
maiores_que_cinco = list(filter(lambda x: x > 5, z))
print(f"Lista de elementos em z maiores que cinco: {maiores_que_cinco}")

# Usando 'reduce' para somar todos os elementos
from functools import reduce
soma_total = reduce(lambda x, y: x + y, z)
print(f"Soma total dos elementos em z usando reduce: {soma_total}")

# Encontrado a maior palavra com reduce

palavras = ["casa", "computador", "sol", "python"]

maior = reduce(lambda x, y: x if len(x) > len(y) else y, palavras)

print(maior)