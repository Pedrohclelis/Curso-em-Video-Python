import time
import random

print('-=' * 11)
print('!!! PEDRA PAPEL E TESOURA !!!')
print('Suas opçoes: \n[ 0 ] Pedra \U0001F44A \n[ 1 ] Papel \U0001F91A \n[ 2 ] Tesoura \U0001F596')
a = int(input('Qual é sua jogada? '))
while a != 0 and a != 1 and a != 2:
    print('\033[1;31mNumero invalido! Por favor digite novamente (0, 1 ou 2)')
    a = int(input('\033[mQual é sua jogada? '))
itens = ['Pedra \U0001F44A', 'Papel\U0001F91A', 'Tesoura \U0001F596']
b = random.randint(0, 2)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
print('-=' * 11)
print(f'Jogador jogou {itens[a]}')
print(f'Computador jogou {itens[b]}')
print('-=' * 11)

if b == a:
    print('\033[1;33mEMPATE \U0001F610')
elif b == 0:
    if a == 1:
        print('\033[1;32mVITORIA \U0001F603')
    else:
        print('\033[1;31mDERROTA \U0001F62A')
elif b == 1:
    if a == 0:
        print('\033[1;31mDERROTA \U0001F62A')
    else:
        print('\033[1;32mVITORIA \U0001F603')
elif b == 2:
    if a == 0:
        print('\033[1;32mVITORIA \U0001F603')
    else:
        print('\033[1;31mDERROTA \U0001F62A')