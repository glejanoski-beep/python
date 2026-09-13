# A função range() gera uma sequecia imutável de números.
# É uma forma muito eficiente para criar sequênias númericas para usar em loops.
# pois não armazena todos os números na memória de uma vez.
# controlar quantas vezes o for vai executar.


'''             exemplos

# Exemplo 1: usando apenas o 'stop'
# gera um sequência de 0 a 4 ( o 5 não é incluído).
print("---range(5)---")
for numero in range(5):
    print(numero)

# Exemplo 2: Usando 'Start' e 'Stop'
# gera um sequência de 2 a 7 (o 7 não é incluído).
print("\n---range(2, 7)---")
for numero in range(2,7):
    print(numero)

# Exemplo 3: Usando 'Start, 'Stop' e 'Step'
# gera uma sequência de números pares de 0 a 10.
print("\n---range(0, 11, 2)---")
#for numero in range(0,11,2):
# gera uma sequencia de numeros impares de 1 a 9.
for numero in range(1,11,2):
    print(numero)

# Exemplo 4: Criando uma contagem regressiva
# O 'Step' negativo, inverte a ordem.
print("\n---range(5, 0, -1)---")
for numero in range(5, 0, -1):
    print(f"Contagem regressiva: {numero}")
print("Fogo!")


'''

# O que é um objeto range?
# A função range() cria um objetp especial do tipo 'range', não uma lista.
meu_range = range(10)
print(f"\nO tipo do objeto criado eh: {type(meu_range)}")
print(f"O objeto em si: {meu_range}")

# Para visualizar todos os números de uma vez, podemos converter o range para uma lista.
lista_de_numeros = list(meu_range)
print(f"O objeto range convertido para lista: {lista_de_numeros}")
