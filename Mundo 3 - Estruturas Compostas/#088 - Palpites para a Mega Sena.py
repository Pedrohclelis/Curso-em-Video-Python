from random import sample
import time

print("=" * 30)
print("SORTEADOR MEGA-SENA")
print("=" * 30)

dados = []

n = int(input("Quantos jogos vc quer que eu sorteie? "))
for jogos in range(1, n+1):
    jogo = sample(range(1, 61), 5) #Cria uma lista com 5 objetos randomizados e nao repetidos cada um de 1-60
    dados.append(jogo[:]) #Faz o backup do jogo nos dados
    jogo.clear() #Limpa o jogo
    print(f"Jogo {jogos}: {sorted(dados[jogos-1])}")
    time.sleep(0.3)



'''n = int(input("Quantos jogos vc quer que eu sorteie? "))
jogo = []
for jogos in range(1, n+1):
    while True:
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
        if len(jogo) >= 6:
            break

    dados.append(jogo[:])
    jogo.clear()
    print(f"Jogo {jogos}: {sorted(dados[jogos-1])}")
    time.sleep(0.3)'''
