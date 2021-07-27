'''n = int(input('Digite um numero para calcular seu fatorial(!): '))
print(f'Calculando {n}! = ', end='')
f = 1
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}') #ou math.factorial(n)'''

n = int(input('Digite um numero para calcular seu fatorial(!): '))
print(f'Calculando {n}! = ', end='')
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}') #ou math.factorial(n)