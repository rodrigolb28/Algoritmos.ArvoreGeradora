import random

n=0

def printGrafo(matriz):
    N = int(input("Digite o número de vértices: "))
    for i in range (n-1):
        for j in range(n-1):
            print(matriz[i][j])


def criarGrafo():
    matriz = []
    n = int(input("Digite o número de vértices: "))
    for i in range (n-1):
        for j in range(n-1):
            matriz[i][j] = random.randint(1, n)
            print(matriz[i][j])
            print(f"Elemento i: {i}, Elemento j: {j}")
        print("\n")

    # printGrafo(matriz)


def calculaArestasGrafoDenso(n):
    num_arestas_denso = (n*(n-1))/2     # calcula o número de arestas
    return num_arestas_denso


def calculaArestasGrafoEsparso(n):
    num_arestas_esparso = (n-1)*4       # calcula o número de arestas
    return num_arestas_esparso




criarGrafo()