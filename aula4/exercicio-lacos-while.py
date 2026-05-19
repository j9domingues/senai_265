## While e utilizado quando nao sabemos o numero de iteracoes que o codigo deve ser executado, ou seja, quando nao sabemos quantas vezes o codigo deve ser repetido.

nome = input("Digite seu nome: ")

while nome == "":
    print("O nome nao pode ser vazio, digite novamente.")
    nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")