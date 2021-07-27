from time import sleep
from random import randint
print("Olá, eu sou seu computador")
sleep(1.25)
print("Por acaso eu tenho um nome?")
sleep(1.5)
print("Poderia dizer meu nome?")
sleep(1.25)
pc = str(input("Digite o nome do seu computador: ")).strip()
print(f"Ah então meu nome é {pc}?")
sleep(1.5)
print("Okay então... Você quer brincar comigo?")
sleep(1.4)
op = str(input("[S/N]")).strip().upper()
while op != "S/N":
    if op == "S":
        sleep(0.75)
        print("Okay, então vamos brincar! (^-^) ")
        sleep(0.5)
        print("Então vamos pro jogo:")
        sleep(0.25)
        print("ele é simples. \n")
        sleep(0.25)
        print("Vou pensar em um número de 0 à 10. \n")
        sleep(0.25)
        print("E você vai tentar advinhar!")
        sleep(0.25)
        print("Então vamos nessa!")
        sleep(0.25)
        comp = randint(0, 10)
        acertou = False
        palpites = 0
        while not acertou:
            jogador = int(input("Qual é o seu palpite? "))
            palpites += 1
            if jogador == comp:
                acertou = True
            else:
                if jogador < comp:
                    print("Você errou... mas você ainda pode continuar tentando \n"
                          "Vou te dar uma dica é um pouco maior que o número que você escolheu \n")
                elif jogador > comp:
                    print("Você errou... mas você ainda pode continuar tentando \n"
                          "Vou te dar uma dica é um pouco menor que o número que você escolheu \n")
        print("Aeeee você ganhou meus parabéns!\n"
              f"Depois de {palpites} tentativas, você me venceu kkkkkk")
        break
    elif op == "N":
        print("Que pena! (T-T) ")
        break
    else:
        print("Eu não entendi, poderia digitar novamente?")
        op = str(input("[S/N]")).strip().upper()