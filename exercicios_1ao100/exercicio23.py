idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar.")
elif idade >= 16 and idade <= 17:
    print("Voto Opcional")
elif idade >= 18 and idade <= 69:
    print("Voto obritório")
else:
    print("Voto Opcional")

'''
TESTE 1 
Digite sua idade: 15
Não pode votar.

TESTE 2 
Digite sua idade: 17 
Voto Opcional

TESTE 3
Digite sua idade: 18
Voto obritório

TESTE 4 
Digite sua idade: 70
Voto Opcional



'''
    