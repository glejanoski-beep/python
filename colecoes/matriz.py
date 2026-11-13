# Soma de Matrizes 3x3

print("="*60)
print("SOMA DE MATRIZES 3x3")
print("="*60 + "\n")

# 1. Exemplo básico: Soma de duas matrizes 3x3
print("1. SOMA BÁSICA DE DUAS MATRIZES 3x3:\n")

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(matriz1)
for linha in matriz1:
    print(linha)

    resultado = [
    [matriz1[0][0] + matriz2[0][0], matriz1[0][1] + matriz2[0][1], matriz1[0][2] + matriz2[0][2]],
    [matriz1[1][0] + matriz2[1][0], matriz1[1][1] + matriz2[1][1], matriz1[1][2] + matriz2[1][2]],
    [matriz1[2][0] + matriz2[2][0], matriz1[2][1] + matriz2[2][1], matriz1[2][2] + matriz2[2][2]]
]

print("\nMatriz 1 + Matriz 2:")
for linha in resultado:
    print(linha)


def somar_matrizes(mat1, mat2):
    