print('=' * 50)
print('BANCO DOS CRIAS'.center(50,' '))
print('=' * 50)

valor = int(input('Qual valor vc quer sacar? R$'))
print(f'{valor//50} cedulas de 50')
valor = valor % 50
print(f'{valor//20} cedulas de 20')
valor = valor % 20
print(f'{valor//10} cedulas de 10')
valor = valor % 10
print(f'{valor//1} cedulas de 1')

'''valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')'''