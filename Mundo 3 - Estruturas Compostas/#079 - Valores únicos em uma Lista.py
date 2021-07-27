lista = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        print(f"O valor {valor} foi armazenado com sucesso!")
        lista.append(valor)

    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        resp = str(input("Nao entendi... Quer continuar ou não? [S/N] "))

lista.sort()
print(f"Voce digitou os valores {lista}")
