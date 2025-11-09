# Descrição: Este programa solicita dois números como entrada do usuário e realiza as quatro operações matemáticas básicas: adição, subtração, multiplicação e divisão.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("\nEscolha a operação que deseja realizar:")
print("1 - Soma")
print("2 - Subtração (valor absoluto)")
print("3 - Multiplicação")
print("4 - Divisão (valor absoluto, 2 casas decimais)")

opcao = input("Digite o número da operação: ")

if opcao == "1":
    soma = num1 + num2
    print("Soma:", soma)
elif opcao == "2":
    subtracao = abs(num1 - num2)
    print("Subtração:", subtracao)
elif opcao == "3":
    multiplicacao = num1 * num2
    print("Multiplicação:", multiplicacao)
elif opcao == "4":
    if num2 != 0:
        divisao = round(abs(num1 / num2), 2)
        print("Divisão:", divisao)
    else:
        print("Erro: divisão por zero.")
else:
    print("Opção inválida.")
