 # :.2f limita o numero de casas decimais 

#  CONVERSOR DE PESO - MODO FAZENDEIRO 

print("=== Conversor de Peso - Modo Fazendeiro ====\n")

peso = float(input("Digite o peso em kg: "))
unidade = input("Digite a unidade de peso (kg para arrobas): ").upper() # o upper é para converter a string para maiúscula, assim o usuário pode digitar tanto "kg" quanto "KG" e o programa vai entender 
if unidade == "K" or unidade == "KG":
    arrobas = peso / 15
    print(f"O peso em arrobas é: {arrobas:.1f} arrobas")
elif unidade == "A":
    kg = peso * 15
    print(f"O peso em kg é: {kg:.1f} kg")
else:    
    print("Unidade de peso inválida! Por favor, digite 'K' para converter de kg para arrobas ou 'A' para converter de arrobas para kg.")