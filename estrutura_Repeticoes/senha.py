senha = 'python'
palpite = ''

while  palpite.lower() != senha:
    palpite = input('Digite a palavra secreta: ')
    if palpite.lower() == senha:
        print(f'Para béns Mizeravi! A palavra secreta é {senha}')
    elif palpite.lower() == 'sair':
        print(f'Covarde!! Desistiu')
        break
    else:
        print(f'Pra que joogar bola na Maavi? Joga de novo, Arroganthi')