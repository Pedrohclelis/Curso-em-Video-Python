from random import randint

def sortear5():
    for position in range(0, 5):
        list.append(randint(1, 10))
    print(f"5 valores sorteados na lista: {sorted(list)}")

def somaPar():
    soma = 0
    for v in list:
        if v % 2 == 0:
            soma += v
    print(f"Somando os valores pares de {sorted(list)} temos que a soma é {soma}")

list = []
sortear5()
somaPar()