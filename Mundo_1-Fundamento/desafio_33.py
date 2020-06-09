#maior e menor de três números sem estrutura de repetição

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

#menor
if n1 <= n2 and n1 <= n3:
    print('O menor número é: {}'.format(n1))
if n2 <= n1 and n2 <= n3:
     print('O menor número é: {}'.format(n2))
if n3 <= n1 and n3 <= n2:
    print('O menor número é: {}'.format(n3))

#maior
if n1 >= n2 and n1 >= n3:
    print('O maior número é: {}'.format(n1))
if n2 >= n1 and n2 >= n3:
    print('O maior número é: {}'.format(n2))
if n3 >= n2 and n3 >= n2:
    print('O maior número é: {}'.format(n3))