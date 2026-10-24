num = int(input('Digite um numero:'))
soma = 0
validacao = num * (num + 1 )/ 2

for i in range(num+1):
    soma += i

print(soma)
print(validacao)
    