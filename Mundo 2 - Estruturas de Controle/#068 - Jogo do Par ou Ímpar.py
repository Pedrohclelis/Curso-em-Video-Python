import random
import time

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(60,' '))
print('Acumule o maximo de vitorias possiveis em 3 vidas'.center(60,' '))
print('=-' * 30)
pc = random.randint(0,10)
n = int(input('\nQual sua jogada? '))
k = str(input('Par ou Impar? [P/I] ')).strip()[0]
while k not in 'PpIi':
    k = str(input('Não entedi... Par ou Impar? [P/I] ')).strip()[0]
vidas = 3
win = 0
while True:
    if n < 0:
        break
    if k in 'Pp':
        if (pc + n) % 2 == 0:
            print(f'Voce jogou {n} e o computador {pc}. Total de {n+pc} deu PAR')
            print('\033[1;32m>>> Você VENCEU !!! \033[m\n')
            win += 1
            time.sleep(0.5)
            print('Vamos jogar novamente...')
            pc = random.randint(0, 10)
            n = int(input('Qual sua jogada? '))
            k = str(input('Par ou Impar? [P/I] ')).strip()[0]
            while k not in 'PpIi':
                k = str(input('Não entedi... Par ou Impar? [P/I] ')).strip()
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total de {n + pc} deu IMPAR')
            print('\033[1;31m>>> Você PERDEU \U0001F494	\033[m\n')
            vidas -= 1
            if vidas == 0: break
            time.sleep(0.5)
            print(f'Cuidado, restam {vidas} vidas')
            print('Vamos jogar novamente...')
            pc = random.randint(0, 10)
            n = int(input('Qual sua jogada? '))
            k = str(input('Par ou Impar? [P/I] ')).strip()[0]
            while k not in 'PpIi':
                k = str(input('Não entedi... Par ou Impar? [P/I] ')).strip()[0]
    if k in 'Ii':
        if (pc + n) % 2 == 0:
            print(f'Voce jogou {n} e o computador {pc}. Total de {n + pc} deu PAR')
            print('\033[1;31m>>> Você PERDEU \U0001F494	\033[m\n')
            vidas -= 1
            if vidas == 0: break
            time.sleep(0.5)
            print(f'Cuidado, restam {vidas} vidas')
            print('Vamos jogar novamente...')
            pc = random.randint(0, 10)
            n = int(input('Qual sua jogada? '))
            k = str(input('Par ou Impar? [P/I] ')).strip()[0]
            while k not in 'PpIi':
                k = str(input('Não entedi... Par ou Impar? [P/I] ')).strip()[0]
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total de {n + pc} deu IMPAR')
            print('\033[1;32m>>> Você VENCEU !!!  \033[m\n')
            win += 1
            time.sleep(0.5)
            print('Vamos jogar novamente...')
            pc = random.randint(0, 10)
            n = int(input('Qual sua jogada? '))
            k = str(input('Par ou Impar? [P/I] ')).strip()[0]
            while k not in 'PpIi':
                k = str(input('Não entedi... Par ou Impar? [P/I] ')).strip()[0]

print('\033[1;31m=' * 60)
print('FIM DE JOGO'.center(60,' '))
if win == 1:
    print(f"              Você venceu \033[1;92m{win}\033[1;31m vez".center(60,' '))
else:
    print(f"              Você venceu \033[1;92m{win}\033[1;31m vezes".center(60,' '))
print('\033[1;31m=' * 60)