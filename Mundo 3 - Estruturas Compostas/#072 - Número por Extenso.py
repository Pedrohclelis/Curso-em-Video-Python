extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinte', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o numero {extenso[n]}")