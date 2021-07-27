from datetime import date
ma = 0
me = 0

for c in range(1,8):
    nasc = int(input(f'Ano que a {c} pessoa nasceu: '))
    if date.today().year - nasc > 18:
        ma += 1
    else:
        me += 1
print(f'Ao todo tivemos {ma} adultos e {me} menores de idade')