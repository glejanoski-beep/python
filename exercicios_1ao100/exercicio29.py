a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))




if a < (b + c) and b < (a + c) and c < (a + b):
    if a ==b and b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Não formam um triangulo")


'''
TESTE 1
Digite o primeiro valor: 555
Digite o segundo valor: 555
Digite o terceiro valor: 555
Equilátero

TESTE 2 
Digite o primeiro valor: 5
Digite o segundo valor: 5
Digite o terceiro valor: 3
Isóceles

TESTE 3
Digite o primeiro valor: 3
Digite o segundo valor: 4
Digite o terceiro valor: 5
Escaleno

TESTE 4 
Digite o primeiro valor: 1
Digite o segundo valor: 2
Digite o terceiro valor: 3
Não formam um triangulo

'''