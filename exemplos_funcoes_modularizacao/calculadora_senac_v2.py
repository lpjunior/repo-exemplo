def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro. Divisão por zero não é permitida.")
        return None
    return a / b

def ler_numero(mensagem):
    valor = input(mensagem).replace(",", ".")
    return float(valor)

def mostrar_menu():
    print("\nEscolha a operação:")
    print("1) soma")
    print("2) subtração")
    print("3) multiplicação")
    print("4) divisão")
    print("5) sair")

print("=== Calculadora Senac ===")

while True:
    mostrar_menu()
    opcao = input("Opção: ")

    if opcao == "5":
        print("Encerrando. Até a próxima.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    # Entrada dos números
    a = ler_numero("Digite o primeiro número: ")
    b = ler_numero("Digite o segundo número: ")

    # Calculo da operação
    if opcao == "1":
        resultado = somar(a, b)
        simbolo = "+"
    elif opcao == "2":
        resultado = subtrair(a, b)
        simbolo = "-"
    elif opcao == "3":
        resultado = multiplicar(a, b)
        simbolo = "*"
    else:
        resultado = dividir(a, b)
        simbolo = "/"

    print(f"Resultado: {a} {simbolo} {b} = {resultado}")