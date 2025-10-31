"""
for -> repetição com quantidade conhecida
while -> repetição enquanto a condição for verdadeira

3 x 12

1..3 -> laço de repetição para serie
1..12 -> laço de repetição para exercicio

para cada elemento(ou valor) em uma sequência de valores:
    execute um conjunto de instruções

for elemento in faixa_de_valores:
    faça_algo

for -> indica o início de uma repetição e qual estrutura estamos usando (for|while)
elemento -> é a variável que recebe cada valor de sequência
in -> significa "dentro de"
faixa_de_valores -> é o conjunto de elementos a serem percorridos (pode ser uma lista, string, inteiros, booleanos, etc.)
faça_algo -> representa o que será executado a cada repetição
"""

for i in range(1, 11):
    print(f"Contagem: {i}")

for s in range(1, 4): # serie
    for e in range(1, 13): # exercício
        print(f" Exercício: {s}x{e}")

"""
1. Contagem de 1 a 10:
tipo: for simples
Objetivo: Imprimir os números de 1 a 10 na tela.
"""
for n in range(1, 11):
    print(n)
"""
2. Tabuada de um número:
tipo: for simples
Objetivo: Solicitar ao usuário um número e imprimir a tabuada desse número de 1 a 10.
"""
# Solicta um número ao usuário
num = int(input("Digite um número para ver a tabuada: "))

# Imprime a tabuada do número de 1 a 10
print(f"Tabuada do {num}:")

# Laço de repetição para calcular e imprimir a tabuada
for multiplicador in range(1, 11): # para cada número de 1 até menor que 11
    resultado = num * multiplicador
    print(f"{num} x {multiplicador} = {resultado}")

"""
3. Soma de números pares:
tipo: for com condição
Objetivo: Calcular a soma dos números pares de 1 a 100.
"""
soma_pares = 0 # variável para armazenar a soma dos números pares

# Laço de repetição para percorrer os números de 1 a 100
for numero in range(1, 101):
    if numero % 2 == 0: # verifica se o número é par
        soma_pares = soma_pares + numero # adiciona o número par à soma

print(f"A soma dos números pares de 1 a 100 é: {soma_pares}")

# versão alternativa usando while
soma_pares = 0 # variável para armazenar a soma dos números pares
numero = 1 # variável para controlar o laço

while numero <= 100:
    if numero % 2 == 0: # verifica se o número é par
        soma_pares = soma_pares + numero # adiciona o número par à soma
    numero += 1 # incrementa o número para a próxima iteração
print(f"A soma dos números pares de 1 a 100 é: {soma_pares}")

# Exemplo de uso do while
# Menu de sistemas

while True: # loop infinito
    operacao = input("Digite a operação desejada (somar, subtrair, multiplicar, dividir) ou 'sair' para encerrar: ")
    if operacao == "somar":
        print("Você escolheu somar.")
    elif operacao == "subtrair":
        print("Você escolheu subtrair.")
    elif operacao == "multiplicar":
        print("Você escolheu multiplicar.")
    elif operacao == "dividir":
        print("Você escolheu dividir.")
    elif operacao.lower() == 'sair':
        print("Programa encerrado.")
        break # sai do loop
    else:
        print("Opção inválida. Tente novamente.")