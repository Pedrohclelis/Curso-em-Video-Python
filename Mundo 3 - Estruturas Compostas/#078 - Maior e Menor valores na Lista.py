lista = []

for p in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posiçao {p}: ")))
print(f"Voce digitou os valores {lista}")

print(f"O maior valor digitado foi {max(lista)}, aparecendo {lista.count(max(lista))} vez(es) nas posições ", end='')
for indice, numero in enumerate(lista):
    if numero == max(lista):
        print(f"{indice}... ", end='')
print(f"\nO menor valor digitado foi {min(lista)}, aparecendo {lista.count(min(lista))} vez nas posições ", end='')
for indice, numero in enumerate(lista):
    if numero == min(lista):
        print(f"{indice}... ", end='')
