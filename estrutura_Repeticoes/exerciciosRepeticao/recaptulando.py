
# Faça um programa que receba dois números inteiros e mostre qual deles é maior.
'''
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))

if num1 > num2:
    print(f"O primeiro número ({num1}) eh maior.")
elif num1 < num2:
    print(f"O segundo numero ({num2}) eh maior")
else:
    print("São iguais.")

'''

# Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número
# for positivo, calcule a raiz quadrada do número e apresente-a. Se o numero for negativo,
# mostre uma menagem dizendo que o número é inválido.
'''
numero = int(input("Digite um numero:"))

if numero < 0:
    print("Numero inválido")
else:
    print(numero ** 0.5)

'''

# Faça um programa que receba um número inteiro e informe se este número é part ou ímpar.

num = int(input("Digite um numero:"))

if num % 2 == 0:
    print(f"O numero {num} eh par!")
else:
    print(f"O numero {num} eh impar!")
