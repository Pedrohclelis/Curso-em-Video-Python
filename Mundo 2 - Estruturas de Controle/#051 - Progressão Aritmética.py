print('=' * 20)
print('\033[1;32m10 TERMOS DE UMA PA\033[m')
print('=' * 20)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(0, 10):
    print(f'{a1 + c *r}', end=' -> ')
print(f'\033[4;31mACABOU \U0001F44C')