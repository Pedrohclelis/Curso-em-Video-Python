def leia(txt):
    valor = str(input(txt)).replace(',', '.')
    while valor.isalpha() == True or valor.strip() == '':
        print(f'ERRO: "{valor}" é um preco invalido')
        valor = str(input(txt))
    return float(valor)