def ficha(nome='<desconhecido>', gols=0):

    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

n = str(input("Nome: ")).capitalize().strip()
g = str(input("No de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    n = '<desconhecido>'


ficha(n, g)