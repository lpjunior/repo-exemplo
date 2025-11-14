from exemplos_funcoes_modularizacao.funcoes.operacoes import somar, subtrair, multiplicar, dividir, modulo


def ler_numero(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida, tente novamente.")

def mostrar_menu():
    print("\nEscolha a operação:")
    print("1) soma")
    print("2) subtração")
    print("3) multiplicação")
    print("4) divisão")
    print("5) modulo")
    print("6) sair")

def executar():
    print("=== Calculadora Senac ===")
    while True:
        mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "6":
            print("Encerrando. Até a próxima.")
            break

        if opcao not in ["1", "2", "3", "4", "5"]:
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
        elif opcao == "4":
            resultado = dividir(a, b)
            simbolo = "/"
        else:
            resultado = modulo(a, b)
            simbolo = "%"

        print(f"Resultado: {a} {simbolo} {b} = {resultado}")

if __name__ == "__main__":
    executar()