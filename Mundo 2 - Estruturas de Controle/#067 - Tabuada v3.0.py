while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        print('-=' * 19)
        print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE')
        break
    print('-=' * 19)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c:2}')