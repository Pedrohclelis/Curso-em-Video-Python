from datetime import date

dados = {}

dados['Nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados['Idade'] = date.today().year-nasc
dados['CT'] = int(input("Carteira de Trabalho [0 nao tem]: "))
if dados['CT'] != 0:
    dados['AnoC'] = int(input("Ano de contratação: "))
    dados['Salario'] = int(input("Salario: "))
    dados['Aposentadoria'] = (dados['AnoC'] + 35) - nasc

for k, v in dados.items():
    print(f"{k}: {v}.")