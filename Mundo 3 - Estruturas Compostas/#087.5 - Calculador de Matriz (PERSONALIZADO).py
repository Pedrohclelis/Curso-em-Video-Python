matriz = []

linha = int(input("Numero de linhas: "))
coluna = int(input("Numero de colunas: "))
print(f"Será uma matriz {linha}x{coluna}")

for i in range(1, linha+1):
    matriz.append(list())

for i in range(1, linha+1):
    for j in range(1, coluna+1):
        matriz[i-1].append(int(input(f"Digite o termo a[{i}, {j}]: ")))

print('-=' * 20)
print("Sua matriz ficou: ")
for i in range(1, linha+1):
    for j in range(1, coluna+1):
        print(f"[{matriz[i-1][j-1]:^3}]", end=' ')
    print()
print('-=' * 20)
