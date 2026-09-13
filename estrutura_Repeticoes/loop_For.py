
'''
print("--- Iterando sobre uma lista de frutas---")
frutas = ["maça", "banana", "laranja", "morango"]
for fruta in frutas:
    print(f"A fruta da vez eh: {fruta}")
'''

'''
print("---Iterando sobre uma string---")
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")
'''
'''
print("---utilizando range(5)---")
for numero in range(5):
    print(f"Numero: {numero}")
'''

'''
print("---Utilizado range de 1 a 5")
for numero in range(1, 6):
    print(f"Numero: {numero}")
'''


'''
print("---Iterando sobre um dicionario de contatos---")
contatos = {
    "João": "joao@email.com",
    "Maria": "maria@email.com",
    "Pedro": "pedro@email.com"
}

print("\n---Nomes (chaves) no dicionario:")
for nome in contatos:
    print(nome)

print("\nEmail (valoes) no dicionario:")
for email in contatos.values():
    print(email)

print("\nContatos completos (chaves e valor:)")
for nome, email in contatos.items():
    print(f"O email {email} pertence ao {nome}")
'''
print("--- Usando enumerate para listar o ranking de filmes---")
filmes_ranking = ["O Poderoso Chefão", "Um Sonho de Liberdade", "Batman: O Cavaleiro das Trevas"]
for i, filme in enumerate(filmes_ranking):
    print(f"#{i + 1}: {filme}")