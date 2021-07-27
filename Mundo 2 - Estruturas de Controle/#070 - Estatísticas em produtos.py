print('-' * 30)
print('LOJA SUPER BARATAO'.center(30,' '))
print('-' * 30)
total = caro = cont = barP = 0
barN = ''

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço: R$'))
    cont += 1
    if cont == 1:
        barN = nome
        barP = preco
    if preco < barP:
        barP = preco
        barN = nome
    total += preco
    if preco > 1000:
        caro += 1
    resp = str(input('Quer continuar: [S/N] ')).strip()[0]
    if resp not in 'Ss':
        if resp in 'Nn':
            break
        else:
            resp = str(input('Nao entendi. Quer continuar: [S/N] ')).strip()[0]

print(' FIM DO PROGRAMA '.center(30,'-'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1.000,00')
print(f'O mais barato foi {barN} que custa {barP}')
