login = input ("Login: ")
senha = input ("Senha: ")

while True:
        if login == "admin" and senha == "1234":
         print("Bem-vindo, admin!")
         break

        elif login == "admin" and senha != "1234":
            while True:
             print("Senha incorreta. Tente novamente.")
             break
        else:
            print("Login ou senha incorreto. Tente novamente.")