#cálculo de par ou ímpar

numero = float(input('Digite um número: '))
calc = numero % 2
if calc == 0:
    print('O número que você digitou é Par')
else: 
    print('O número que você digitou é Ímpar')