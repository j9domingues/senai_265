idade = int(input("Qual é a sua idade? "))

if idade < 13:
    print("Crinaça")

elif idade <18:
    print("Adolescente")

elif idade <65:
    print("Adulto")
    
else:
    print("Idoso")