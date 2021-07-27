#1o jeito: maximo e minimo da lista

lista = []
for c in range(1,6):
    peso = float(input(f'Peso da {c} pessoa: '))
    lista += [peso] #ou lista.append(peso)
print(f'Os pesos foram: {lista}')
print('O Maior peso foi:', max(lista))  #maximo valor da lista
print('O Menor peso foi:', min(lista))  #minimo valor da lista

#2o jeito: ordenando a lista

lista2 = []
for c in range(1,6):
    peso2 = float(input(f'Peso da {c} pessoa: '))
    lista2 += [peso2] #ou lista.append(peso)
lista2.sort() #ordenar a lista em ordem crescente
print(f'Os pesos foram: {lista2}')
print(f'O Maior peso foi: {lista2[0]}')
print(f'O Menor peso foi: {lista2[4]}')