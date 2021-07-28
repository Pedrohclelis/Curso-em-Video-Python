dados = {}
dados['Nome'] = str(input("Nome: "))
dados['media'] = float(input(f"Media de {dados['Nome']}: "))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'Recupe'
else:
    dados['situacao'] = 'reprovado'

for key, value in dados.items():
    print(f"{key} é igual a {value}")