lista = []
par = []
impar = []

while True:
    num = int(input("Digite um numero: "))
    lista += [num]
    if num % 2 == 0:
        par += [num]
    else:
        impar.append(num)
    resp = str(input("Quer continuar? [S/N] ")).strip()
    while resp not in 'SsNn':
        resp = str(input("Nao entendi... Quer continuar ou não? [S/N] ")).strip()
    if resp in 'Nn':
        break

print(f"Lista completa: {lista}")
print(f"Lista par: {sorted(par)}")
print(f"Lista impar: {sorted(impar)}")
