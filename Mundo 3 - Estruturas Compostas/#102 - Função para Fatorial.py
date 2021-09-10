def fatorial(n, show=False):
    cont = 1
    for num in range(n , 0, -1):
        if show:
            print(f"{num} x ", end='')
        cont *= num
    return cont

print(fatorial(5, True))