print('Olá, mundo!!')
print("Primeiro passo na programação Python.")

nome = 'Luis'
numero = 10

# f-string - formatação de string
print(nome + ' camisa ' + str(numero) + '.')
print(f'{nome} camisa {numero}.')

'''
Exercícios:

1. Saudação Simples
Crie variaveis com seu nome e sua a idade, depois imprima uma saudação usando essas variáveis.
'''

nome = 'Luis'
idade = 38
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
'''
2. Soma de dois números
Atribua dois números a variáveis, depois imprima o resultado da soma.
'''

a = 7
b = 8
soma = a + b

print("A soma de ", a, "e", b, "é", soma)
print("A soma de " + str(a) + " e " + str(b) + " é " + str(soma))
print(f"A soma de {a} e {b} é {a + b}")

'''
3. Mistura de tipos
Use variáveis de tipos diferentes e imprima todas juntas
'''

nome = 'Luis'
idade = 38
altura = 1.87

print(f"O {nome} tem {idade} anos e altura {altura}.")


# ------------------------------------------------------------------------

# 1. print() usando virgula
nome = "Wagner"
idade = 25
print("Meu nome é", nome, "e eu tenho", idade, "anos.")

# 2. print() concatenando (+)
nome = "Pamela"
idade = 18
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")

# 3. print usando str.format()
nome = "Carlos"
idade = 28
peso = 70.333333333

print("Meu nome é {} e eu tenho {} anos e peso {}.".format(nome, idade, peso))
print("Meu nome é {n} e eu tenho {i} anos e peso {p:.2f}.".format(p=peso, i=idade, n=nome))

# 4. print() usando f-string
nome = "João"
idade = 35
altura = 1.78
peso = 75.8888888
print(f"Meu nome é {nome} e eu tenho {idade} anos, peso {peso:.1f} e tenho {altura} de altura.\nEu terei no ano que vem {idade + 1} anos de idade.")


"""
1. [f-string] Mostre na tela uma frase como:
    "Olá, Luis! Você tem 38 anos."

   Continue o código:
   nome = input("Digite seu nome: ")
   idade = int(input("Digite sua idade: "))
   # Escreva o print usando f-string aqui
"""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá, {nome}! Você tem {idade} anos.")

"""
2. [concatenação] Peça ao usuário o nome de uma cidade e de um estado. Mostre:
   "Você mora em São Paulo, SP."

   Continue o código:
   cidade = input("Digite o nome da cidade: ")
   estado = input("Digite o estado: ")
   # Escreva o print com concatenação(+) aqui
"""
cidade = input("Digite o nome da cidade: ")
estado = input("Digite o estado: ")
print("Você mora em " + cidade + ", " + estado + ".")
"""
3. [virgula] Crie variaveis e mostre:
    "O gato tem 4 anos."
    
   Continue o código:
   animal = 'gato'
   idade = 4
   # Escreva o print usando virgula(,) aqui
"""
animal = 'gato'
idade = 4
print("O", animal, "tem", idade, "anos.")

"""
4. [.format()] Crie variáveis e mostre:
    "As notas foram 8.5 e 9.0, a média é 8.75."
    
   Continue o código:
   nota1 = 8.5
   nota2 = 9.0
   media = (nota1 + nota2)/2
   # Escreva o print usando .format() aqui
"""
nota1 = 8.5
nota2 = 9.0
media = (nota1 + nota2) / 2
print("As notas foram {} e {}, a média é {:.2f}.".format(nota1, nota2, media))

# if condicacao -> a condição sempre espera uma verdade
idade = 16
if idade >= 18:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

nome = 'Paulo'
if nome == 'Luis':
    print("Olá, Luis!")
else:
    print("Você não é o Luis.")

"""
    estrutura de decisão (if, elif, else)
    estrutura simples (if)
    estrutura composta (if, else)
    estrutura encadeada (if, elif, else)

    estrutura simples ela dada pelo seguinte cenário:
    se a condição for verdadeira, faça algo
    se a condição for falsa, não faça nada

    if condição:
        faça algo

    ------------------------------------------------------------
    estrutura composta ela dada pelo seguinte cenário:
    se a condição for verdadeira, faça algo
    se a condição for falsa, faça outra coisa
    
    if condição:
        faça algo
    else:
        faça outra coisa
        
    ------------------------------------------------------------
    estrutura encadeada ela é dada pelo seguinte cenário:
    se a primeira condição for verdadeira, faça algo
    se a for falsa, testa uma nova condição, faça algo
    se nenhuma for verdadeira, faça outra coisa (opcional)
    
    if condição: nota >= 6
        faça algo #aprovado
    elif condição22: nota >= 5
        faça algo #recuperação
    else: # opcional
        faça outra coisa #reprovado
        
    URA: Unidade de Resposta Audível
    print("disk 1 para..)
    print("disk 2 para..)
    print("disk 3 para..)
    print("disk 4 para..)
        
    if opcao == 1: financeiro
    elif opcao == 2: suporte
    elif opcao == 3: 2 via do boleto
    elif opcao == 4: outros
    elif opcao == 9: falar com atendente
    else: opção invalida
    
    --------------------------------------------------------------
"""

"""
Peça ao usuário para digitar um número inteiro.
O programa deve verificar se o número é maior que zero.
Se for, mostre a mensagem:
"O número é positivo."
"""
numero_positivo = int(input("Digite um número inteiro: "))
if numero_positivo > 0:
    print("O número é positivo.")
elif numero_positivo == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")
"""
Peça ao usuário para digitar um número inteiro.
O programa deve verificar se o número é par ou ímpar.
Mostre a mensagem:
"O número é par." se o número for divisível por 2.
"O número é ímpar." caso contrário.
"""
numero_par_impar = int(input("Digite um número inteiro: "))
if numero_par_impar % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

"""
Peça ao usuário para digitar uma nota entre 0 e 10.
O programa deve mostrar a seguinte mensagem:
- Excelente, se a nota for maior ou igual a 9.
- Bom, se a nota for maior ou igual a 7 e menor que 9.
- Regular, se a nota for entre 5 e 6,9.
- Insuficiente, se a nota for menor que 5.
"""
nota = float(input("Digite uma nota entre 0 e 10: "))
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")

"""
Mostre o seguinte menu na tela:
1 - somar
2 - subtrair
3 - multiplicar
4 - dividir

Peça ao usuário para escolher uma opção (1, 2, 3 ou 4).
- "Você escolheu somar." se a opção for 1.
- "Você escolheu subtrair." se a opção for 2.
- "Você escolheu multiplicar." se a opção for 3.
- "Você escolheu dividir." se a opção for 4.
- "Opção inválida." para qualquer outro número.
"""
print("Menu:")
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
opcao = int(input("Escolha uma opção (1, 2, 3 ou 4): "))

if opcao == 1:
    print("Você escolheu somar.")
elif opcao == 2:
    print("Você escolheu subtrair.")
elif opcao == 3:
    print("Você escolheu multiplicar.")
elif opcao == 4:
    print("Você escolheu dividir.")
else:
    print("Opção inválida.")

""""
   Tipos de dados:
    tipos inteiros (1, 2, 3...) -> tipo int
    tipos reais (1.5, 2.5, 3.5...) -> tipo float
    tipos texto ('a', 'b', 'c'...) -> tipo str
    tipos booleano (True, False) -> tipo bool
   
   Operadores lógicos:
    and (e) -> todas as condições devem ser verdadeiras
    or (ou) -> pelo menos uma condição deve ser verdadeira
    not (não) -> inverte o valor lógico (True vira False e vice-versa)

AND (p and q)
 p | q | resultado
 v | v | v
 v | f | f
 f | v | f
 f | f | f

OR (p or q)
 p | q | resultado
 v | v | v
 v | f | v
 f | v | v
 f | f | f
 
NOT (not p)
 p | resultado
 v | f
 f | v
"""

# Exemplos de operadores lógicos
idade = 20 # inteiro (int)
habilitacao = True # booleano (bool)

# O teste da condição é feito da esquerda para a direita
# O resulto do teste lógico é True ou False
if idade >= 18 and habilitacao: # ambas as condições devem ser verdadeiras
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

"""
Atividade 5 - Entrada gratuita
Objetivo: usar operadores lógicos.
Crie um programa que pergunte a idade do usuário e se é estudante.
A entrada é gratuita se a pessoa tiver menos de 12 anos ou for estudante.
Mostre a mensagem:
"Entrada gratuita." se a pessoa tiver menos de 12 anos ou for estudante.
"Entrada paga." caso contrário.
"""
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? (s/n): ").strip().lower()
if idade < 12 or estudante == 's':
    print("Entrada gratuita.")
else:
    print("Entrada paga.")

porta_trancada = False

if not porta_trancada:
    print("Tranque a porta antes de sair!")