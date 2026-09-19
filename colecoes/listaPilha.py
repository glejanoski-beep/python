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

def inverter_string(texto):
    pilha = []

    # Empilhando caracter
    for caracter in texto:
        pilha.append(caracter)

    # Desempilhar para inverter
    invertido = ''
    while len(pilha) > 0:
        invertido += pilha.pop()

    return invertido

texto_original = 'Python'
texto_invertido = inverter_string(texto_original)

print(f'Texto Original: {texto_original}')
print(f'Texto Invertido: {texto_invertido}')

print('\n' + '='*55 + '\n')

# 5 - Verificando parênteses balanceados

print('5 - Verificando parênteses balanceados')
print('='*55)

def parenteses_balanceados(expressao):
    pilha = []
    pares = {'(': ')', '[': ']', '{': '}'}

    for caracter in expressao:
        if caracter in pares:               # Abre
            pilha.append(caracter)
        elif caracter in pares.values():    # Fecha
            if len(pilha) == 0:
                return False
            abre = pilha.pop()
            if pares[abre] != caracter:
                return False

    return len(pilha) == 0

expressoes = [
    '((a + b) * c)',
    '([{a}])',
    '((a + b)',
    '([)]',
    '{ a + [ b * (c / d)]}'
]

for expr in expressoes:
    resultado = parenteses_balanceados(expr)
    status = 'Balanceado' if resultado else 'Nao balanceado'
    print(f'{expr:20} -> {status}')


print('\n' + '='*55 + '\n')

# 6 - Desfazer (undo) / refazer (redo)

print('SISTEMA DE DESFAZER/REFAZER\n')

class EditorTexto:
    def __init__(self):
        self.historico_desfazer = []
        self.historico_refazer = []
        self.texto = ''

    def adicionar_texto(self, texto):
        self.historico_desfazer.append(self.texto)
        self.texto += texto
        self.historico_refazer = []  # Limpa redo
        print(f" + texto adicionado: '{self.texto}'")

    def desfazer(self):
        if len(self.historico_desfazer) > 0:
            self.historico_refazer.append(self.texto)
            self.texto = self.historico_desfazer.pop()
            print(f'Refeito: {self.texto}\n')
        else:
            print('Nada para desfazer\n')

    def refazer(self):
        if len(self.historico_refazer) > 0:
            self.historico_desfazer.append(self.texto)
            self.texto = self.historico_refazer.pop()
            print(f'Desfeito: {self.texto}')
        else:
            print('Nada para refazer')

    def mostrar_texto(self):
        print(f'Texto atual: {self.texto}')


editor = EditorTexto()

editor.adicionar_texto('hello')
editor.adicionar_texto('World')
editor.mostrar_texto()
print()

editor.desfazer()
editor.mostrar_texto()
print()

editor.refazer()
editor.mostrar_texto()
print()

editor.adicionar_texto(' ')
editor.adicionar_texto('!')
editor.mostrar_texto()

# 7 - Comparação PILHA vs FILA

print('Comparação pilha vs fila\n')

print('Pilha (stack) - LIFO:')
print('ultimo a entrar, primeiro a sar')
print('Usa append() e pop()')
print('Exemplos: historico, undo/redo, navegação')

print()

print('FILA (Queue) - FIFO:')
print('primeiro a entrar, primeiro a sar')
print('usa append() e pop(0)')
print('Exemplos: fila de atendimento, processamento de tarefas\n')

# 8 - Converter para decimal usando pilha

print('\n' + '='*55 + '\n')
print('Converter para decimal usando pilha')
print('='*55)

def binario_para_decimal(binario_str):
    pilha = []
    potencia = 0

    # Coloca cada código na pilha
    for digito in binario_str:
        pilha.append(int(digito))

    # Remove da pilha (de tras para frente) e calcula
    decimal = 0
    while len(pilha) > 0:
        digito = pilha.pop()
        decimal += digito * (2 ** potencia)
        potencia += 1

    return decimal

binarios = ['101', '1010', '11111', '10000']

for bin_num in binarios:
    decimal = binario_para_decimal(bin_num)
    print(f'{bin_num} (binario) = {decimal} (decimal)')

