print('-' * 30)
print('CADASTRE UMA PESSOA'.center(30,' '))
print('-' * 30)
adultos = homens = novinha = 0
while True:
    i = int(input('Idade: '))
    if i > 18:
        adultos += 1
    s = str(input('Sexo: [H/M] ')).strip().upper()[0]
    if s in 'Hh':
        homens += 1
    if s in 'Mm':
        if i < 20:
            novinha += 1
    if s not in 'HhMm':
        s = str(input('Invalido. Sexo: [H/M] ')).strip().upper()[0]
    r = str(input('Quer continuar? [S/N]')).strip()[0]
    if r not in 'Ss':
        if r in 'Nn':
            break
        else:
            r = str(input('Invalido. Quer continuar? [S/N]')).strip()[0]
print(f'O total de pessoas com mais de 18 anos é {adultos}')
print(f'Ao todos temos {homens} homens cadastrados')
print(f'E {novinha} mulheres abaixo de 20 anos')