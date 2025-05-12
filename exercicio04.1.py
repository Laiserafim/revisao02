soma = 0
for x in range (5):
    num = int(input("Digite o número: "))
    soma = soma + num
media = soma / 5
print(f"Média = {media}")
if media >= 7:
    print("Aprovado!")
elif media < 4 :
    print("Reprovado! ")
elif media>=4 and media<7:
    print("Recuperação!")
else:
    print("Número inválido!")