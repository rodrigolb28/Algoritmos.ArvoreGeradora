N=0

def printGrafo(matriz):
    N = int(input("Digite o número de vértices: "))
    for i in range (N-1):
        for j in range(N-1):
            print(matriz[i][j])


def criarGrafo():
    matriz = []
    N = int(input("Digite o número de vértices: "))
    for i in range (N-1):
        for j in range(N-1):
            matriz[i][j] = i+j

    printGrafo(matriz)

criarGrafo()








criarGrafo()