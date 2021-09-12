def leiaInt(texto):
    while True:
        num = str(input(texto)).strip()
        try:
            return int(num)
        except ValueError:
            print("\033[31mErro de valor: ", end='')
        except TypeError:
            print("\033[31mErro de tipo: ", end='')
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida", end='')
            return 0
        print(f"'{num}' nao é um inteiro valido!\033[m")

def leiaReal(txt):
    while True:
        num = str(input(txt))
        try:
            return float(num)
        except ValueError:
            try:
                num = num.replace(',', '.')
                return float(num)
            except:
                print("\033[31mErro de valor: ", end='')
        except TypeError:
            print("\033[31mErro de tipo: ", end='')
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida", end='')
            return 0
        print(f"'{num}' nao é um inteiro valido!\033[m")


while True:
    i = leiaInt('Digite um numero inteiro: ')
    print(f'Voce digitou o numero inteiro {i}')
    r = leiaReal('Digite um numero real: ')
    print(f'Voce digitou o numero real {r}')
    print()

