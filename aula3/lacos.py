estoque = ["prego", "porca", "parafuso", "arruela", "mola"]
procurar = input("Digite o item que deseja procurar: ").lower() # o lower é para converter a string para minúscula, assim o usuário pode digitar tanto "Prego" quanto "prego" e o programa vai entender
for item in estoque:
    if item == procurar:
        print("Item encontrado: ", item)
        break # interrompe o laço imediatamente após encontrar o item.
else:    
    print("Item não encontrado no estoque.")