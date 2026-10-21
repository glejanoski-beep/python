num = int(input('Digite um valor:'))
contador = 0

while contador <= 10:
    resultado = num * contador
    print(f'{num} * {contador} = {resultado}')
    contador+=1