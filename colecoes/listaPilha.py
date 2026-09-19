# Usando Listas como Pilhas (LIFO - last in, first ou)

# Uma pilha é uma estrutura de dados onde o ultimo elemento a entrar
# é o primeiro a sair (LIFO - Last in, First out)
# Em Python, podemos usar listas para implementar pilhas com append() e pop().


# 1 - Exemplo básico de pilha

print('='*50)

pilha = []
print('Pilha vazia', pilha)

# Adicionando elementos (emplilhando)

pilha.append('Livro 1')
pilha.append('Livro 2')
pilha.append('Livro 3')
pilha.append('Livro 4')
print('\nApos adicionar os livros:', pilha)

# Removendo elementos (desempilhando)

topo = pilha.pop()
print(f'\nRemovendo o livro do topo: {topo}')
print('Apos remover topo:', pilha)

topo = pilha.pop()
print(f'\nRemovendo o livro do topo: {topo}')
print('Apos remover topo:', pilha)

print('='*50)

# 2 - Simulação de navegação no browser (histórico)

historico = []

def visitar_pagina(pilha, url):
    pilha.append(url)
    print(f'Visitando: {url}')

def voltar_pagina(pilha):
    if len(pilha) > 1:
        pilha.pop()  # Removendo pagina atual
        pagina = pilha[-1] # Pega a anterior
        print(f'Voltando para: {pagina}')
        return pagina
    elif len(pilha) == 1:
        print('Sem historico anterior!')
        return None
    else:
        print('Historico vazio')
        return None

# Navegando em páginas

visitar_pagina(historico, 'https://google.com')
visitar_pagina(historico, 'https://github.com')
visitar_pagina(historico, 'https://python.org')
visitar_pagina(historico, 'https://stackoverflow.com')

print(f'\nHistorico atual: {historico}\n')

# Voltando páginas
voltar_pagina(historico)
print(f'Historico: {historico}\n')

voltar_pagina(historico)
print(f'Historico: {historico}\n')

voltar_pagina(historico)
print(f'Historico: {historico}\n')

voltar_pagina(historico)

print('='*50)

# 3 - Verificando o elemento do topo sem remover

print('------- Pilha de pratos---------')

pratos = []

def empilhar_pratos(pilha, cor):
    pilha.append(cor)
    print(f'+ prato {cor} adicionado!')

def desempilhar_prato(pilha):
    if len(pilha) > 0:
        prato = pilha.pop()
        print(f'- prato {prato} removido.')
        return prato
    else:
        print(f'Nenhum prato na pilha.')
        return None

def topo_pilha(pilha):
    if len(pilha) > 0:
        return pilha[-1]
    else:
        return None

def pilha_vazia(pilha):
    return len(pilha) == 0

# Operações
empilhar_pratos(pratos, 'azul')
empilhar_pratos(pratos, 'branco')
empilhar_pratos(pratos, 'vermelho')

print(f'\nprato do topo: {topo_pilha(pratos)}')
print(f'Total de pratos: {len(pratos)}')
print(f'Pilha vazia? {pilha_vazia(pratos)}\n')

print()
desempilhar_prato(pratos)
desempilhar_prato(pratos)
desempilhar_prato(pratos)
print(f'\nPilha vazia agora? {pilha_vazia(pratos)}')

print('='*50)

# 4 - Inverter uma string usando pilha