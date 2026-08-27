ano = int(input("Digite um ano: "))

res1 = ano % 400
res2 = ano % 4
res3 = ano % 100 

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("Bissexto")
else:
    print("Não bissexto")

print(res1)
print(res2)
print(res3)

'''
TESTE 1 
Digite um ano: 2023
Não bissexto

TESTE 2 
Digite um ano: 1900
Não bissexto

TESTE 3 
Digite um ano: 2000
Bissexto

TESSTE 4
Digite um ano: 2024
Bissexto

'''