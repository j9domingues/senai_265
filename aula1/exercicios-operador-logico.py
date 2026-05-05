idade = int(input("digite sua idade "))
cnh = input("Você tem CNH? ")

if idade >=  18 and cnh == "sim":
    print("Liberado!")
else:
    print("Bloqueado!")