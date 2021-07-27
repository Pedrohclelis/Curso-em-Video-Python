perfil = []
dados = []
maior = menor = 0

while True:
    nome = str(input("Nome: "))
    perfil.append(nome)
    peso = float(input("Peso: "))
    perfil.append(peso)
    if len(dados) == 0:
        maior = menor = perfil[1]
    else:
        if perfil[1] > maior:
            maior = perfil[1]
        if perfil[1] < menor:
            menor = perfil[1]
    dados.append(perfil[:])
    perfil.clear()
    resp = str(input("Quer continuar? [S/N] "))
    while resp not in 'SsNn':
        resp = str(input("Nao entendi... Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

print("-=" * 30 )
print(f"Ao todo, você cadastrou {len(dados)} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de ", end='')
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print(f"\nO menor peso foi de {menor}Kg. Peso de ", end='')
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')