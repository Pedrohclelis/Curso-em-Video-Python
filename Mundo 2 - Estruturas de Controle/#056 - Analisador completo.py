#Requisitado: NOME e IDADE do homem mais velho, quantas mulheres como menos de 20 anos
media = 0
idadeH = 0
nomeH = ''
msub20 = 0
n = int(input('Quantas pessoas vc deseja analisar? '))
for c in range(1, n+1):
    print(f'----- {c}ª pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexo [H/M]: '))
    if sexo in 'Hh':
        if idade > idadeH:
            nomeH = nome
            idadeH = idade
    if sexo in 'Mm' and idade < 20:
        msub20 += 1

print(f'A media de idade do grupo foi de {media/n:2} anos')
print(f'O homem mais velho tem {idadeH} anos e se chama {nomeH}')
print(f'Ao todo sao {msub20} mulheres com menos de 20 anos')