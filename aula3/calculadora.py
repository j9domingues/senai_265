# para comentar use o alt + ; 
# calculadora simples usando python

print("Calculadora Simples")

num1=float(input("Digite o primeiro número: ")) # o float é para aceitar números decimais, no portugol é REAl
operador=input("Digite o operador (+, -, *, /): ") # o input é para receber um valor do usuário, string é para aceitar texto, no portugol é CARACTER, o operador é a variável que armazena o valor do operador escolhido pelo usuário
num2=float(input("Digite o segundo número: ")) 

if operador == "+": # o == é para comparar, o = é para atribuir um valor a uma variável
    resultado = num1 + num2
    print("O resultado é: ", resultado) # o print é para exibir o resultado na tela, o , é para separar o texto do resultado, o resultado é a variável que armazena o valor da operação
elif operador == "-": # o elif é para criar uma nova condição, o else é para criar uma condição para quando nenhuma das anteriores for verdadeira
    resultado = num1 - num2
    print("O resultado é: ", resultado)
elif operador == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
elif operador == "/": 
    if num2 == 0: # para evitar a divisão por zero, que é uma operação inválida
        print("Erro: Divisão por zero não é permitida!")
    resultado = num1 / num2 
    print("O resultado é: ", resultado)
else:
    print("Operador inválido!")