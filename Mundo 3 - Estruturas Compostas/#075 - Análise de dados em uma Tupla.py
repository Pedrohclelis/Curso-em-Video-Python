pares = 0

tupla = tuple(int(input('Digite um numero: ')) for c in range(0,4))
print(f"Voce digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O primeiro numero 3 apareceu na posicao {tupla.index(3)+1}")
else:
    print("Nao ha valor 3")
print("Os valores parem sao: ", end='')
for n in tupla:
    if n % 2 == 0:
        print(f"{n}", end= ' ')
        pares += 1
print(f"Totalizando {pares} pares")