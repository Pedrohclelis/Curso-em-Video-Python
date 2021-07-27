print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos vc quer mostrar? '))
cont = 0
a = 1
b = 1
print('0 -> 1 -> 1 -> ', end='')
while cont != termos-3:
    c = a+b
    print(c, end=' -> ')
    cont += 1
    a = b
    b = c
print('FIM')
