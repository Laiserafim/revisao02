frase = input("Digite uma frase: ")
cont=0
for i in frase:
    if i == "a":
        cont= cont + 1
print(f"A frase tem {cont} letra A ")