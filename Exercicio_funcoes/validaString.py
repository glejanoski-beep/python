

def valida_string (palavra, min, max):
    texto = palavra
    valor_minimo = min
    valor_maximo = max

    if len(texto) <= valor_maximo and len(texto) >= valor_minimo:
        return  True
    else:
        return False



texto = input('Digite um texto:')

# comentado para tornar o valor minimo e maximo, respectivamente (1 e 100)
# minimo = int(input('Digite o minimo de caracters aceitos no texto:'))
# maximo = int(input('Digite o maximo de caracters aceitos no texto:'))

funcao = valida_string(texto, 1, 100)
print(funcao)








