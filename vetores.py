nome = 'Luis'
lista_de_compras = ['maçã', 'banana', 'laranja', 'sabão', 'arroz']
lista_de_numeros = [10, 23, 45, 67, 89, 12, 34]

print("Lista de compras:")
print(lista_de_compras)

print("\nNúmeros na lista:")
print(lista_de_numeros)

frutas = ['maçã', 'banana', 'laranja', 'uva', 'pera']
frutas.append('abacaxi')  # Adiciona 'abacaxi' ao final da lista)
print(frutas)
print(frutas[0])
print(frutas[3])

"""
    em uma lista temos índices e posição para cada elemento.
    índice: começa em 0 (n-1)
    posição: começa em 1 (n)
    O índice é usado para acessar os elementos da lista. E a posição é usada para referenciar a ordem dos elementos.
"""

alunos = []
alunos.append('Wagner')
alunos.append('Pamela')
alunos.append('Carlos')
alunos.append('Nielsen')
alunos.insert(1, 'Pedro')  # Insere 'Pedro' na posição 2 (índice 1))
alunos[0] = 'Roberto' # Altera o primeiro elemento para 'Roberto'

print(alunos)
print(f'O tamanho da lista de alunos é: {len(alunos)}')

# Percorrendo a lista de alunos usando for e range(), utilizando os índices
print("Lista de alunos:")
for i in range(len(alunos)): # 0 1 2 3 ... len(alunos)-1
    print(f'Aluno {i + 1}: {alunos[i]}')

"""
Como funciona:
1. len(alunos) retorna o tamanho da lista alunos.
2. range(len(alunos)) cria uma sequência de números de 0 até o tamanho da len(alunos) - 1.
3. Dentro do for, você acessa cada elemento com alunos[i], onde i é o índice atual do loop.
"""

# funções e métodos principais para listas

# Lista base
numeros = [5, 2, 9, 1, 5, 6]

# append() - adiciona um elemento ao final da lista
numeros.append(9)
print("append:", numeros) # [5, 2, 9, 1, 5, 6, 9]

# insert() - insere um elemento em uma posição específica
numeros.insert(2, 7)
print("insert:", numeros) # [5, 2, 7, 9, 1, 5, 6, 9]

# remove() - remove a primeira ocorrência de um elemento
numeros.remove(9)
print("remove:", numeros) # [5, 2, 7, 1, 5, 6, 9]

# pop() - remove e retorna o último elemento da lista (ou o elemento em uma posição específica)
ultimo = numeros.pop()
print("pop:", numeros, "| removido:", ultimo) # [5, 2, 7, 1, 5, 6] | removido: 9

# len() - retorna o tamanho da lista
print("len:", len(numeros)) # 6

# sort() - ordena os elementos da lista
numeros.sort()
print("sort (crescente):", numeros) # [1, 2, 5, 5, 6, 7]

numeros.sort(reverse=True)
print("sort (decrescente):", numeros) # [7, 6, 5, 5, 2, 1]

# reverse() - inverte a ordem dos elementos na lista
numeros.reverse()
print("reverse:", numeros) # [1, 2, 5, 5, 6, 7]

# index() - retorna o índice da primeira ocorrência de um elemento
print("index de 5:", numeros.index(5)) # 2

# count() - conta quantas vezes um elemento aparece na lista
print("count de 5:", numeros.count(7)) # 1

# copy() - cria uma cópia da lista
copia = numeros.copy()
print("copy:", copia) # [1, 2, 5, 5, 6, 7]

# clear() - remove todos os elementos da lista
numeros.clear()
print("clear:", numeros) # []

# split() - divide uma string em uma lista com base em um delimitador
frase = "O rato roeu a roupa do rei de Roma"
palavras = frase.split()  # Divide por espaços
print("split:", palavras) # ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']

csv = "1;3;4;5;6;7;89;0;10"
valores = csv.split(";")  # Divide por ponto e vírgula
print("split com (;):", valores) # ['1', '3', '4', '5', '6', '7', '89', '0', '10']

nomes = "Ana,Bruno,Carlos,Diana"
lista_nomes = nomes.split(",")  # Divide por vírgula
print("split com (,):", lista_nomes) # ['Ana', 'Bruno', 'Carlos', 'Diana']

texto = "um-dois-três-quatro"
partes = texto.split("-", 2)  # Divide por hífen, no máximo 2 vezes
print("split com (-) e limite máximo de splits 2:", partes) # ['um', 'dois', 'três-quatro']

# join() - junta os elementos de uma lista em uma única string
palavras = ["Aprender", "Python", "é", "divertido"]
frase = " ".join(palavras)  # Junta com espaço
print("join com espaço:", frase) # "Aprender Python é divertido"