def leiaInt(texto):
    num = str(input(texto)).strip()
    while num.isnumeric() == False:
        print("ERRO! Digite um numero inteiro valido!")
        num = str(input(f'{texto}')).strip()
    return int(num)

n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}')