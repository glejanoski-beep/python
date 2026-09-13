# O loop 'while' executa um bloco de código repetidamente,
# contando que uma determinada condição seja verdadeira.

'''
 -------------- Sintaxe --------------

 while condição:
    bloco de código que será executado

É fundamental garantir que a condição se torne falsa em algum momento,
para evitar um loop infinito.
'''
'''
# Exemplo 1: Contagem simples
# O loop continuará enquanto 'contador'for menor ou igua a 5.
print("---- Contagem de 1 a 5 ----")
contador = 1
while contador <= 5:
    print(f"Contador está em: {contador}")
    contador += 1 # Incrementamos o contador para que ele eventualmente chegue a 6 e pare o loop.
'''

'''
# Exemplo 2: Loop controlado por entrada do usuário
print("--- Advinhe a palavra secreta ---")
palavra_secreta = "Python"
palpite = ""

while palpite.lower() != palavra_secreta:
    palpite = input("Advinhe a palavra secreta (ou digite 'sair'):")
    if palpite.lower() == "sair":
        print("Você saiu do jogo")
        break # O comando 'break' interrompe o loop imediatamente
    elif palpite.lower() == palavra_secreta.lower():
        print("Parabéns! Acertou a palavra secreta!")
        break # mesmo acertando o jogo não parava
    else:
        print("Palpite incorreto! Tente novamente.")

print("Game Over")
'''
'''
# Exemplo 3: Usando 'continue' para pular um interação
# Vamos imprimir apenas os números ímpares de 1 a 10.
print("--- Imprimindo números impares ---")
numero = 0
while numero < 10:
    numero += 1 
    if numero % 2 == 0:     # se o numero for par
        continue            # o 'continue' pula o resto do código e vai para proxima iteração
    print(f'Numero ímpar: {numero}')
'''

# Exemplo 4: clausula 'else' no loop while
# o bloco 'else' é executado com o o loop termina normalmente (sem interrompimento por um 'break')
tentativa = 3
while tentativa > 0:
    print(f"Você tem {tentativa} tentativas.")
    # aqui poderia ter a logica de um jogo, tentativas de acesso...
    tentativa -= 1
#else:
print("O loop termininou porque as tentativas acabaram (sem 'break')")