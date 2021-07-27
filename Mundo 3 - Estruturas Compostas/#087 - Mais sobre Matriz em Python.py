matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = j3 = 0

for i in range(0,3):
    for j in range(0,3):
        n = int(input(f"Digite o valor para [{i}, {j}]: "))
        matriz[i][j] = n
        if n % 2 == 0:
            pares += n
        if j == 2:
            j3 += n

for i in range(0,3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^4}] ", end='')
    print()

print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da 3a coluna (j = 3) é {j3}")
print(f"O maior valor da 2a linha (i = 2) é {max(matriz[2])}")