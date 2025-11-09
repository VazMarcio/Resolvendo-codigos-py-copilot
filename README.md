# Resolvendo-codigos-py-copilot

# 🧠 Projeto: Resolvendo-codigos-py-copilot

Este projeto foi desenvolvido com o objetivo de praticar e solucionar algoritmos simples utilizando a linguagem Python e as sugestões inteligentes do GitHub Copilot. Cada arquivo representa um exercício de lógica e manipulação de dados, com foco em entrada de dados, operações matemáticas, manipulação de strings e estruturas condicionais.

---

## 📁 Arquivos Criados

- `Concat_dados.py`
- `Ope_mat.py`
- `Repet_txt.py`
- `Num_par_impar.py`
- `Media_notas.py`
- `Palindromos.py`

---

## 📄 `Concat_dados.py`

```python
info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")
dados_concatenados = info1 + " " + info2
print("Dados concatenados:", dados_concatenados)
````

## 🔍 Explicação
- Solicita duas informações do usuário.

- Concatena as duas strings com um espaço entre elas.

- Exibe o resultado da concatenação.

## 📄 `Ope_mat.py`

````python
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
````
## 🔍 Explicação
- Recebe dois números inteiros.

- Exibe um menu de operações.

- Executa a operação escolhida com tratamento de erros e arredondamento.

## 📄 `Repet_txt.py`

````python
texto = input("Digite uma string: ")
num_repeticoes = int(input("Digite um número inteiro: "))
resultado = (texto +  " ") * num_repeticoes
print("Resultado:",  resultado)
````

## 🔍 Explicação
- Recebe uma string e um número.

- Repete a string com espaço o número de vezes informado.

- Exibe o resultado.

## 📄 `Num_par_impar.py`

````python
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")    
`````
## 🔍 Explicação
- Verifica se o número é par ou ímpar usando o operador %.

- Exibe o resultado com interpolação de string.

## 📄 `Media_notas.py`

````python
# Solicita ao usuário que insira três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))    

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média calculada
print("A média das notas é:", media)

````

## 🔍 Explicação
- Recebe três notas decimais.

- Calcula a média aritmética.

- Exibe o resultado.

## 📄 `Palindromos.py`

````python
# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")
# Inverte a palavra
palavra_invertida = palavra[::-1]
# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
````

## 🔍 Explicação
- Inverte a palavra usando slicing.

- Compara a palavra original com a invertida.

- Verifica se é um palíndromo.

## ✅ O que foi aprendido
# Entrada de dados com input()

- Conversão de tipos com int() e float()

- Manipulação de strings e concatenação

- Operações matemáticas básicas

- Uso de estruturas condicionais if/elif/else

- Verificação de paridade com %

- Lógica para identificar palíndromos

- Repetição de texto com multiplicação de strings

##🧾 Conclusão
Este projeto foi uma excelente introdução à lógica de programação com Python. Utilizando as sugestões do GitHub Copilot, foi possível criar scripts simples, funcionais e educativos. Cada exercício reforça conceitos fundamentais da linguagem e estimula o raciocínio lógico.

👤 Autor do Projeto
- Márcio Vaz 
- 📧 Email: githubmarcio@gmail.com


