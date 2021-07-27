lista = []
cont = 0

while True:
    num = int(input("Digite um numero: "))
    lista += [num]
    cont += 1
    resp = str(input("Quer continuar? [S/N] "))
    while resp not in 'SsNn':
        resp = str(input("Nao entendi... Quer continuar ou não? [S/N] "))
    if resp in 'Nn':
        break

print(f"Voce digitou {cont} elementos")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if 5 in list:
    print(f"O valor 5 está na lista")