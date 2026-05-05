idade = int(input("Qual a sua idade? "))
condicacao_fisica = input("Qual a sua condição física? ")
atestado_medico = input("Você possui atestado médico? ")

if idade >= 18 and (condicacao_fisica == "boa" or atestado_medico =="sim"):
    print("Liberado")
else:
    print("Bloqueado")