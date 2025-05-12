segredo = 1234
senha = 0
while senha != segredo:
    senha = int(input("Senha: "))
    if senha == segredo:
        print("Acesso liberado! ")
