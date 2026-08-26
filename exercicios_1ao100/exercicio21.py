nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2 

if media >= 7:
    print(f"Parabéns! Você foi aprovado. Média: {media}")
else:
    print(f"Não foi dessa vez! Reprovado. Média: {media}")


'''
TESTE 1
Digite a primeira nota: 5
Digite a segunda nota: 8
Não foi dessa vez! Reprovado. Média: 6.5

TESTE 2
Digite a primeira nota: 8
Digite a segunda nota: 7
Parabéns! Você foi aprovado. Média: 7.5

TESTE 3
Digite a primeira nota: 7.5
Digite a segunda nota: 6.5
Parabéns! Você foi aprovado. Média: 7.0

TESTE 4
Digite a primeira nota: 7.5
Digite a segunda nota: 6.4
Não foi dessa vez! Reprovado. Média: 6.95

'''