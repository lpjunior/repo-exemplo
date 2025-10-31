"""
Exercício: Gerenciador de Alunos
Descrição:
Crie um programa que gerencie uma lista de alunos em uma turma.
O programa deve permitir ao usuário inserir nomes,
organizar e manipular a lista usando os métodos estudados.

Passo a passo para resolver o exercício:
1. Peça ao usuário que digite os nomes dos alunos separados por vírgula.
2. Mostre:
    - Quantos alunos foram cadastrados
    - O nome do primeiro e do último aluno da lista
3. Peça ao usuário para adicionar mais um aluno no final da lista.
4. Peça ao usuário para adicionar um aluno no início da lista.
5. Peça ao usuário para remover um aluno pelo nome.
6. Mostre a lista de alunos em ordem alfabética.
7. Inverta a ordem da lista e mostre o resultado.
8. Faça uma cópia da lista original e limpe a original.
9. Mostre ambas as listas para o usuário.
"""
# 1. Entrada dos nomes
entrada = input("Digite os nomes dos alunos separados por vírgula: ")
alunos = entrada.split(",")  # Divide a string em uma lista
print(f"Nomes cadastrados: {alunos}")

# Removendo espaços extras
alunos = [aluno.strip() for aluno in alunos]

print("\nLista inicial de alunos:", alunos)

# 2. Informações sobre básicas
print(f"Quantidade de alunos cadastrados: {len(alunos)}")
print(f"Primeiro aluno: {alunos[0]}")
print(f"Último aluno: {alunos[-1]}")

# 3. Adicionar novo aluno
novo = input("Digite o nome de um novo aluno para adicionar ao final da lista: ")
alunos.append(novo.strip())

# 4. Inserir no início
inicio = input("Digite o nome de um aluno para adicionar no início da lista: ")
alunos.insert(0, inicio.strip())

# 5. Remover aluno
remover = input("Digite o nome do aluno que deseja remover: ")
if remover.strip() in alunos:
    alunos.remove(remover.strip())
    print(f"Aluno {remover.strip()} removido.")
else:
    print(f"Aluno {remover.strip()} não encontrado na lista.")

# 6. Ordenar lista
alunos.sort()
print("\nLista de alunos em ordem alfabética:", alunos)

# 7. Inverter lista
alunos.reverse()
print("Lista de alunos em ordem inversa:", alunos)

# 8. Cópia e limpeza
copia_alunos = alunos.copy()
alunos.clear()

# 9. Mostrar listas
print("\nLista original limpa:", alunos)
print("Cópia da lista original:", copia_alunos)

