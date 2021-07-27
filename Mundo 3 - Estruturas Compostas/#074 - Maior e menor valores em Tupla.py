from random import randint

tupla = ()
i = int(input("Sua tupla tem quantos caracteres aleatorios? "))

tupla = tuple(randint(1, 100) for num in range(0, i))

print(tupla) #prova real
print(f"Os valores sorteados foram: ", end='')
for c in range(0, i):
    print(tupla[c], end=' ')

print(f"\nO maior valor sorteado foi: {sorted(tupla)[-1]}. Sua 1a ocorrencia é na posiçao {tupla.index(max(tupla))+1} ")      #ou {max(tupla)}
print(f"O menor valor sorteado foi: {sorted(tupla)[1]}. Sua 1a ocorrencia é na posiçao {tupla.index(sorted(tupla)[1])+1}")    #ou {min(tupla)}