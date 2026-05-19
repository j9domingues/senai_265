procurar = input("Pesquisar peça: ")
estoque = ["parafuso", "porca", "arruela", "bucha", "prego", "mola"] #lista é uma variavel que guarda mais de um valor, e cada valor tem um indice, ou seja, uma posicao na lista.

for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque!")
        break #break é utilizado para sair do loop, ou seja, para parar a execucao do loop.
else:
        print("Item nao encontrado no estoque.")

