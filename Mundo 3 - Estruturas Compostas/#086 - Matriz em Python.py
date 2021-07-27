matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        n = int(input(f"Digite o valor para [{i}, {j}]: "))
        matriz[i][j] = n

for i in range(0,3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^4}] ", end='')
    print()