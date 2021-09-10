c = ('\033[0;0m', #reset 0
    '\033[1;42m', #verde 1
    '\033[1;107m', #branco 2
    '\033[1;44m', #azul 3
    '\033[1;41m', #vermelho 4
    '\033[1;97m', #txt branco 5
    '\033[1;30m', #txt preto 6
                            )

def ajuda(cmd):
    texto(f"Acessando o manual do comando '{cmd}'", 3)
    print(f"{c[2]}{c[6]}")
    help(cmd)
    print(f"{c[0]}", end='')

def texto(txt, cor):
    print(f"{c[cor]}{c[5]}~" * (len(txt)+4))
    print(f"  {txt}  ")
    print(f"~" * (len(txt)+4))
    print(f"{c[0]}", end='')

while True:
    texto('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input(">>> Funçao ou Biblioteca: "))
    if comando.upper().strip() == 'FIM':
        texto('ATÉ LOGO!', 4)
        break
    ajuda(comando)