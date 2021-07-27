lista = []

exp = str(input("Digite a expressao: "))
lista += exp
if lista.count('(') != lista.count(')') or lista.index('(') > lista.index(')'):
    print("Expressao invalida!")
else:
    print("Expressao valida :D !!!")
print(lista)