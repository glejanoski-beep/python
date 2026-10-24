num = int(input("Digite um numero:"))
ini = int(input("Digite o multiplicador inicial:"))
fim = int(input("Digite o multiplicador final:"))


if fim < ini:     
    for i in range(ini, fim, -1):
        resultado = num * i
        print(f'{num} * {i} = {resultado}')
else:
    for i in range(ini, fim, 1):
        resultado = num * i
        print(f'{num} * {i} = {resultado}')
    

