idade = int(input("Digite a idade: "))
estudante = input("Estudante:\n SIM: (s)\n NAO: (n)\n")

meia_entrada = idade < 12 or idade > 60 or estudante == "s"
ingresso = float(30)

if meia_entrada:
    print (f"Valor do ingresso: {ingresso * .5}")
else:
    print(f"Valor do ingresso: {ingresso}")


'''
TESTE 1
Digite a idade: 10
Estudante:
 SIM: (s)
 NAO: (n)
n
Valor do ingresso: 15.0

TESTE 2
Digite a idade: 25
Estudante:
 SIM: (s)
 NAO: (n)
s
Valor do ingresso: 15.0

TESTE 3
Digite a idade: 65
Estudante:
 SIM: (s)
 NAO: (n)
n
Valor do ingresso: 15.0

TESTE 4
Digite a idade: 30
Estudante:
 SIM: (s)
 NAO: (n)
n
Valor do ingresso: 30.0

TESTE 5
Digite a idade: 11
Estudante:
 SIM: (s)
 NAO: (n)
s
Valor do ingresso: 15.0
'''