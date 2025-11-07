import random

"""
1. Escreva um programa em Python que leia os valores de uma matriz 3x3
fornecidos pelo usuário. O programa deve solicitar, um a um, os elementos de
cada posição da matriz, armazena-los em uma lista de listas e, ao final, exibir
a matriz completa na tela formatado de linhas e colunas.
"""
matriz = []

num_linhas = int(input(f"Digite a quantidade de linhas: "))
num_colunas = int(input(f"Digite a quantidade de colunas: "))

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    for valor in linha:
        print(valor, end=' ')
    print()

"""
2. Elabore um programa que percorra todos os elementos de uma matriz 5x5 e calcule a
soma de seus valores. Ao final, o programa deve exibir na tela o resultado
da soma total de todos os elementos da matriz.
"""
soma = 0
matriz = []

# gerei valores aleatórios para a matriz
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        soma += valor

print(f"A soma de todos os valores é {soma}")

"""
3. Crie um programa que solicite ao usuário o tamanho da matriz, exiba a matriz formatada
e mostre a soma da diagonal principal da matriz.
"""
matriz = []
soma = 0

num_linhas = int(input(f"Digite a quantidade de linhas: "))
num_colunas = int(input(f"Digite a quantidade de colunas: "))

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
 for valor in linha:
     print(valor, end=' ')
 print()

for i in range(len(matriz)):
    soma += matriz[i][i]

print(f"\nMatriz da diagonal principal é: {soma}")