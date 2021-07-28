from random import randint
from operator import itemgetter

jogo = {'jogador 1': randint(1, 21),
        'jogador 2': randint(1, 21),
        'jogador 3': randint(1, 21),
        'jogador 4': randint(1, 21)}

for k, v in jogo.items():
    print(f"O {k} tirou {v} no dado.")

print("\n\tRanking:")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f"{k+1}º lugar: {v[0]} com {v[1]}")