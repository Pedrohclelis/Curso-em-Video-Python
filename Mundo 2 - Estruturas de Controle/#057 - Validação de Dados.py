s = str(input('Digite seu sexo [H/M]: ')).upper().strip()[0]
while s not in 'HhMm':
    s = str(input('Opçao invalida. Digite seu sexo novamente [H/M]: ')).upper().strip()[0]
print(f'Sexo {s} registrado com sucesso!')