lista = []

for p in range(0, 5):
    num = int(input("Digite um valor: "))
    if p == 0 or num > lista[-1]:
        lista.append(num)
        print(f"Adicionado na posiçao {lista.index(num)} lista!")
    else:
        for pos in range(0, len(lista)):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Adicionado na posiçao {lista.index(num)} lista!")
                break
    print(lista)