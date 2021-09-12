from util import moeda
from util import dado

p = dado.leia("Preço a ser lido: R$")
print(f"Voce digitou {moeda.format(p)}")

print(f"A metade de {moeda.format(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.format(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando 10% de {moeda.format(p)} temos {moeda.aumentar(p, 10, True)}")
print(f"Diminuindo 13% de {moeda.format(p)} temos {moeda.diminuir(p, 13, True)}")