def voto(atual):
    from datetime import date
    idade = date.today().year-atual
    if idade < 16:
        return f"Com {idade} anos: NAO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: OPCIONAL"
    return f"Com {idade} anos: OBRIGATORIO"


ano = int(input("Em que ano vc nasceu? "))
print(voto(ano))
