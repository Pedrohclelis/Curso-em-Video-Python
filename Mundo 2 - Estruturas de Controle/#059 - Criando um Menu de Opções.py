from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-=' * 10)
print('    [1] Somar \n    [2] Multiplicar \n    [3] Maior dentre eles \n    [4] Trocar os numeros \n    [5] Sair do programa')
print('=-=' * 10)
c = int(input('>>>>> Qual é sua opção? '))
while c != 5:
    if c == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        c = int(input('>>>>> Qual é sua opção? '))
    elif c == 2:
        print(f'A multiplicaçao de {n1} x {n2} é {n1*n2}')
        c = int(input('>>>>> Qual é sua opção? '))
    elif c == 3:
        print(f'Entre {n1} e {n2} o maior é ')
        c = int(input('>>>>> Qual é sua opção? '))
    elif c == 4:
        print('Informe os numeros novamente \/ ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        c = int(input('>>>>> Qual é sua opção? '))
    else:
        print('Opção inválida, tente novamente!')
        c = int(input('>>>>> Qual é sua opção? '))
print('Finalizando...')
sleep(0.5)
print('Fim do progama! Volte sempre!')
print('=-=' * 10)