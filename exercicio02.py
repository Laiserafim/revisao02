num = 15
resp = 0
while num != resp:
    resp = int (input("Digite um número: "))

    if resp < num:
        print(f"{resp} é menor que que o número esperado.")
    elif resp > num:
        print(f"{resp} é maior que o número esperado.")
    else:
        print("Parabéns! Você acertou o número! ")
