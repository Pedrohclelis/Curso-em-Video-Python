lista = [[], []]

for c in range(1,8):
    num = int(input(f"Digite o {c}º valor numerico: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    print(lista)
print(f"Os valores pares sao: {sorted(lista[0])}")
print(f"Os valores pares sao: {sorted(lista[1])}")