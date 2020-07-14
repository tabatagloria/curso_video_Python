#progressão aritmética com for


t = int(input('Digite o 1º termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
calc = t
for i in range(10):
    print(calc)
    calc = calc + r
    