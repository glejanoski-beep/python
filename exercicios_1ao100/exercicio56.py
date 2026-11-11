invalida = 0

while True:
    nota = int(input('Digite uma nota válida (0 á 10): '))
    if nota < 0 or nota > 10:
        invalida +=1
    else:
        break 

print(f'A nota: {nota}')
print(f'Tentativas inválidas: {invalida}')  
    

print("Aperte 'Enter' para fechar...")

