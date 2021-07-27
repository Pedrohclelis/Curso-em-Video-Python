num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero [999 pra parar]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')
