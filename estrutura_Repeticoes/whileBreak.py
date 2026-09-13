# O comando 'break' serve para interromper a execução de um loop (while ou for)
# de forma imediata, mesmo que a condição do loop ainda seja verdadeira.
# O programa então continua a execução ma primeira linha de código após o loop.


'''
# Exemplo 1: Interrompendo um loop de contagem
print("--- Interrompendo a contagem no 5 ---")
contador = 1
while contador <= 10:
    print(f"Contador: {contador}")
    if contador == 5:
        print("Condição de parada atingida. Usando 'break' para sair.")
        break
    contador += 1
print("Exemplo finalizado!")
'''

'''
# Exemplo 2: Usando 'while true' com 'break'
# Este é um padrão comum para criar um loop que só termina com uma condição específica
while True: # Cria um loop que. a princípio , rodaria para sempre.
    resposta = input("Digite 'sair' para termina o programa:")
    if resposta.lower() == "sair":
        print("Comando 'sair' recebido. Encerrando o loop")
        break       # Unica forma de sair do loop
    else:
        print(f"Você digitou '{resposta}'. O loop continua.")
print("Exemplo 2 finalizado.")
'''


# Exemplo 3: Jogo de adivinhação
# O loop continua se o usuário acertar o número.
print("--- Jogo de adivinhação ---")
numero_secreto = 42

while True:
    try:
        palpite = int(input("Advinhe o numero secreto (1 a 100): "))

        if palpite == numero_secreto:
            print("Parabens! Voce acertou")
            break
        elif palpite < numero_secreto:
            print("Numero secreto eh maior. Tente novamebte")
        else:
            print("Numero secreto eh menor. Tente novamente")

    except ValueError:
        print("Entrada invalida! Por favor, digite um numero.")

print("Game Over")

