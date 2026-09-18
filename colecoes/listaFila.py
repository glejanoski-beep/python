# Usando listas como filas (FIFO - First in, first out)

# Uma fila é uma estrututa de dados onde o primeiro elemento a entrar
# é o primeiro elemento a sair (FIFO - First in, First out)
# Em Python, podemos usar listas para implementar filas com append() e pop().

# 1 - Exemplo básico de fila

fila = []
print('Fila vazia', fila)

# adicionando elementos (enfileirando)
fila.append('pessoa 1')
fila.append('pessoa 2')
fila.append('pessoa 3')
fila.append('pessoa 4')
print('Apos adicionar 4 pessoas:', fila)

# Removendo elementos (desfileirando)
primeira = fila.pop(0)
print('\nPrimeira pessoa a sair:', primeira)
print('resultado fila', fila)

primeira = fila.pop(0)
print('\nSegunda pessoa a sair:', primeira)
print('resultado fila', fila)

print('='*50)

# 2 - Simulação de fila de supermercado

print('='*50)
print('-------- Fila de supermercado --------')
print('='*50)

fila_caixa = []

def adicionar_cliente(fila, nome):
    fila.append(nome)
    print(f'\n{nome} entrou na fila.')

def atender_cliente(fila):
    if len(fila) > 0:
        cliente = fila.pop(0)
        print(f'\n{cliente} foi atendino e saiu da fila')
        return cliente
    else:
        print('Nenhum cliente na fila para atender.')
        return None

# Clientes chegando

adicionar_cliente(fila_caixa, 'ana')
adicionar_cliente(fila_caixa, 'carlos')
adicionar_cliente(fila_caixa, 'bruno')
adicionar_cliente(fila_caixa, 'diana')

print(f'\nFila atual: {fila_caixa}')
print(f'\nQuantidade de clientes na fila:', len(fila_caixa))

atender_cliente(fila_caixa)
print('Fila:', fila_caixa)

atender_cliente(fila_caixa)
print('Fila:', fila_caixa)

atender_cliente(fila_caixa)
print('Fila:', fila_caixa)

atender_cliente(fila_caixa)
atender_cliente(fila_caixa)
print('Fila:', fila_caixa)

print('='*50)

# 3 - Verificando se a fila está vazia ou cheia

print("\n3 - Verificando se a fila está vazia ou cheia")

tarefas = []

def adicionar_tarefa(fila, tarefa):
    fila.append(tarefa)
    print(f'Tarefa adicionada: {tarefa}')
    print(f'Total de tarefas: {fila}\n')

def proxima_tarefa(fila):
    if len(fila) > 0:
        tarefa = fila.pop(0)
        print(f'Executando: {tarefa}')
        print(f'Tarefas restante na fila: {len(fila)}\n')
        return tarefa
    else:
        print('Nenhuma tarefa na fila.')
        return None

adicionar_tarefa(tarefas, 'estudar python')
adicionar_tarefa(tarefas, 'fazer exercicios')
adicionar_tarefa(tarefas, 'revisar conceitos')

print(f'Fila de tarefas: {tarefas}\n')

proxima_tarefa(tarefas)
print()

proxima_tarefa(tarefas)
print()

proxima_tarefa(tarefas)
print()
proxima_tarefa(tarefas)

print('\n'+ '='*50 + '\n')


# 4 - Usando collection.deque para filas mais eficientes

from collections import deque

fila_deque = deque()
print('Deque vazio', fila_deque)


# Adicionando elementos

fila_deque.append(10)
fila_deque.append(20)
fila_deque.append(30)
fila_deque.append(40)
print('Apos adicionar elementos a fila:', fila_deque)

# Remover do inicio (poplef() é mais eficiente que pop(0) com listas)

primeiro = fila_deque.popleft()
print(f'\nPrimeiro elemento saindo: {primeiro}')
print(f'Deque apos remocao: {fila_deque}\n')

segundo = fila_deque.popleft()
print(f'\nSegundo elemento saindo: {segundo}')
print(f'Deque apos remocao: {fila_deque}\n')

print('\n'+ '='*55 + '\n')


# 5 - Pesquisar diferença e quando usar list/deque

# 6 - Exemplo prático: Sistema de processamento de pedidos
print('='*55 )
print('------- Sistema de processamento de pedidos ---------')
print('='*55 )

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente

    def __str__(self):
        return f'Pedido #{self.numero} - Cliente: {self.cliente}'

fila_pedidos = deque()

# Novos pedidos chegando

pedidos = [
    Pedido(1, 'Joao silva'),
    Pedido(2, 'maria santos'),
    Pedido(3, 'pedro costa'),
    Pedido(4, 'ana oliveira')
]

for pedido in pedidos:
    fila_pedidos.append(pedido)
    print(f'{pedido} entrou na fila.\n')

print(f'Total de pedidos: {len(fila_pedidos)}\n')

# Processando pedidos

while len(fila_pedidos) > 0:
    pedido = fila_pedidos.popleft()
    print(f'Processando: {pedido}\n')










