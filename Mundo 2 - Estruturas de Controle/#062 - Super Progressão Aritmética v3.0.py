print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = a1
b = 1
cont = 0
mais = 10
m = 0
while mais != 0:
    while cont < mais:
        print(n, end=' -> ')
        n += r
        cont += 1
    print('PAUSA')
    m += mais
    cont = 0
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print(f'Progressao finalizada com {m} termos mostrados')