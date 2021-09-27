def leiaInt(texto):
    while True:
        num = str(input(texto))
        try:
            num = int(num)
            if num != 1 and num != 2 and num != 3:
                print("ERRO: Opção invalida (Digite apenas 1, 2 ou 3)")
            else:
                return num
        except:
            print(f"ERRO: '{num}' nao é um numero inteiro valido")

def verCad():


while True:
    print("-" * 20)
    print("MENU PRINCIPAL")
    print("-" * 20)
    print("1 - Ver pessoas cadastradas")
    print("2 - Ver pessoas cadastradas")
    print("3 - Sair do sistema")
    print("-" * 20)
    n = leiaInt("Sua opção: ")
    if n = 1:
