nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2 

if media >= 7:
    print(f"Média: {media}. Aprovado.")
elif media < 7 and media > 5:
    print(f"Média: {media}. Recuperação.")
else:
    print(f"Média: {media}. Reprovado.")


'''
TESTE 1
Digite a primeira nota: 4
Digite a segunda nota: 5
Média: 4.5. Reprovado.

TESTE 2
Digite a primeira nota: 8
Digite a segunda nota: 6
Média: 7.0. Aprovado.

TESTE 3 
Digite a primeira nota: 5
Digite a segunda nota: 6
Média: 5.5. Recuperação.


'''