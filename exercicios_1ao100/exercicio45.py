valor = int(input('Digite um valor:'))

def finbonacci(n):
    a = 0
    b = 1
    c = 0

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
        

finbonacci(valor)
print("Aperte 'Enter' para fechar...")