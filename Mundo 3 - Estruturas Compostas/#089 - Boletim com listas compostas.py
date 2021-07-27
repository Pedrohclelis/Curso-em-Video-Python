dados = []
perfil = []
cont = 0

while True:
    cont += 1
    nome = str(input("Nome: ")).strip()
    while nome.isdigit() == True:
        nome = str(input("Nao entendi... Qual seu nome: "))
        if nome.isdigit() == False and nome.isalnum() == True :
            break
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    dados.append([nome, media, [nota1, nota2]])

    resp = str(input("Quer continuar? [S/N] "))
    while resp not in 'SsNn':
        resp = str(input("Nao entendi... Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

print("=-" * 22)
print(f"{'No.':<4} {'NOME':<30} {'MÉDIA':>8}")
print("-" * 44)
for index, dado in enumerate(dados):
    print(f"{index+1:<2} - {dado[0]:<30} {dado[1]:>8.1f}")
print("-" * 44)

while True:
    n = int(input("Mostrar notas de qual aluno? [999 para interromper] "))
    if n == 999:
        break
    if n > len(dados):
        print(f"As notas de {dados[-1][0]} são {dados[-1][2]}")
    else:
        print(f"As notas de {dados[n-1][0]} são {dados[n-1][2]}")
    print("-" * 44)