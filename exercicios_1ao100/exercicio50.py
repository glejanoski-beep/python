maiorvalor: int

for i in range(10):
    val = int(input('Digite um valor:'))
    if i == 0 or maiorvalor < val:
        maiorvalor = val

      
print(f'maior Valor = {maiorvalor}')
print("Aperte 'Enter' para fechar...")