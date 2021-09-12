def dobro(valor=0, formato=False):
    if formato == True:
        return format(valor*2)
    return valor*2


def metade(valor=0, formato=False):
    if formato == True:
        return format(valor/2)
    return valor/2


def aumentar(valor=0, taxa=0, formato=False):
    if formato == True:
        return format(valor*(1+taxa/100))
    return valor*(1+taxa/100)


def diminuir(valor=0, taxa=0, formato=False):
    if formato == True:
        return format(valor*(1-taxa/100))
    return valor*(1-taxa/100)


def format(valor=0, cambio='R$'):
    return f"{cambio.upper()}{valor:.2f}".replace('.', ',')