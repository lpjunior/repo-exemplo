print("=== Calculadora Senac ===")

while True:
    print("\nEscolha a operação:")
    print("1) soma")
    print("2) subtração")
    print("3) multiplicação")
    print("4) divisão")
    print("5) sair")

    opcao = input("Opção: ")

    if opcao == "5":
        print("Encerrando. Até a próxima.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    # Entrada dos números
    a = input("Digite o primeiro número: ").replace(",", ".")
    b = input("Digite o segundo número: ").replace(",", ".")

    # Conversão para float
    a = float(a)
    b = float(b)

    # Calculo da operação
    if opcao == "1":
        resultado = a + b
        simbolo = "+"
    elif opcao == "2":
        resultado = a - b
        simbolo = "-"
    elif opcao == "3":
        resultado = a * b
        simbolo = "*"
    else:
        if b == 0:
            print("Erro. Divisão por zero não é permitida.")
            continue
        resultado = a / b
        simbolo = "/"

    print(f"Resultado: {a} {simbolo} {b} = {resultado}")