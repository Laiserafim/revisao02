segredo = 1234
i = 0
while i != segredo:
    senha = int(input("Senha: "))
    if senha == segredo:
        print("Acesso liberado! ")
        i = senha