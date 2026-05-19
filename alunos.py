alunos = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
aluno = input("Digite o nome do aluno para verificar se está presente: ")
# 
while aluno in alunos:
    print(f"{aluno} está presente.")
    break
else:    print(f"{aluno} não está presente.")