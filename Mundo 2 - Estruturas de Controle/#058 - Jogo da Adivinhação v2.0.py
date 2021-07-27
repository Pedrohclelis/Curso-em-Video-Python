import random

cont = 1
pc = random.randint(0, 10)

print('Sou seu computador... \nAcabei de pensar num numero entre 0 e 10 \nSera que voce consegue advinhar qual foi?')
n = int(input('Qual é seu palpite? '))

while n != pc:
    cont += 1
    if n < pc:
        print('Mais... Tente novamente.')
        n = int(input('Qual é seu palpite? '))
    else:
        print('Menos... Tente novamente')
        n = int(input('Qual é seu palpite? '))

print(f'Acertou após {cont} tentativas, parabens!')
