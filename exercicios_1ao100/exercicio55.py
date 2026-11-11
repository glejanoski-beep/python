primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
quantidade = int(input('Quantidade: '))

soma = 0

print('Sequência:', end=' ')

for i in range(quantidade):
    termo = primeiro + i * razao
    print(termo, end=' ')
    soma += termo

print(f'\nSoma: {soma}')

print("Aperte 'Enter' para fechar...")