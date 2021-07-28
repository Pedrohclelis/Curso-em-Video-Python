from random import randint
from operator import itemgetter
from time import sleep

jogador = dict()
dados = list()
ranking = list()

#Lendo os jogadores e gerando os numeros
print(" ROLADOR DE 1d20 ".center(40, '='))
i = int(input("Quantos jogadores há na mesa? "))
for c in range(0, i):
    jogador['nome'] = str(input('Nome: '))
    jogador['num'] = randint(1, 21)
    dados.append(jogador.copy())

#Mostrando a leitura seca
for k, v in enumerate(dados):
    print(f"O jogador {v['nome']} tirou {v['num']} nos dados.")
    sleep(0.3)
print("\x1B[3malea jacta est...\x1B[0m")

#Rankeando os dados
print()
print(" Ranking ".center(40, '='))
ranking = sorted(dados, key=itemgetter('num'), reverse=True)
for k, v in enumerate(ranking):
    print(f"{k+1}° lugar: {v['nome']}, com {v['num']} pontos.")
    sleep(0.3)