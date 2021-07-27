cont = 0
num = int(input('Digite um numero: '))
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[1;92m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[1;31m{c}\033[m', end=' ')

print(f'\nO numero {num} foi divisivel {cont} vezes')
if cont > 2:
    print('\033[1;35mEntao ele NÃO é primo...')
else:
    print('\033[1;36mPor isso ele É primo')