matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# lembrando que começa por zero (n-1)
#idx_linha = 2
#idx_coluna = 2
##print(matriz[idx_linha][idx_coluna]) # buscando o valor da linha 3 coluna 3
##print(matriz[2]) # buscando a lista 3
##print(matriz) # imprime a matriz
##
##print("\n----------------------\n")

for lista in matriz:
    for valor in lista:
        print(valor, end=" ")
    print()