estudante = input("Vc estuda? ")
idade = int(input("Quantos anos vc tem?"))

if estudante == "sim" or idade >65:
    print("Ganhou desconto!")
else:
    print("Preço normal!")