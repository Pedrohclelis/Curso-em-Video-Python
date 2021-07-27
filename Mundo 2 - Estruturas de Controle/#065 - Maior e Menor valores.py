r = ''
cont = soma = ma = me = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n
print(f'Voce digitou {cont} numeros e a media foi {soma/cont}')
print(f'O maior valor foi {ma} e o menor foi {me}')
