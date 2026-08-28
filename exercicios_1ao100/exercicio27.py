peso = int(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo da faixa")
elif IMC >= 18.5 and IMC < 25:
    print("Faixa normal")
elif IMC >= 25 and IMC < 30:
    print("Acima da Faixa")
else:
    print("Faixa Elevada")


'''
TESTE 1
Digite o peso em quilogramas: 50
Digite a altura em metros: 1.70
Abaixo da faixa

TESTE 2
Digite o peso em quilogramas: 80
Digite a altura em metros: 1.75
Acima da Faixa

TESTE 3
Digite o peso em quilogramas: 90
Digite a altura em metros: 1.70
Faixa Elevada

'''