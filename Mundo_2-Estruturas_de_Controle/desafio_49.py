#tabuada com for

n = float(input('Digite um número: '))
print('Tabuada do número {}'.format(n))
for i in range (0, 11):
    print('{} x {} = {}'.format(i, n, i*n))