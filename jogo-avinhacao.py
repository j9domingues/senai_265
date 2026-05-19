# contador = 0

# for i in range(1000):# Exemplo: repetir 1000 vezes
#     print(i)
#     contador += 1 # incrementa o contador em 1 a cada iteracao do loop


import random

print("=== Adivinhe um número ===")
numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
tentativas = 0
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")