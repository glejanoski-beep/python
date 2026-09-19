

def inverter_string(texto):
    pilha = []

    # Empilhando caracter
    for caracter in texto:
        pilha.append(caracter)

    # Desempilhar para inverter
    invertido = ''
    while len(pilha) > 0:
        invertido += pilha.pop()

    return invertido

palavra = input("Digite uma palavra: ")


print(f'Assim fica a palavra invertira: {inverter_string(palavra)}')