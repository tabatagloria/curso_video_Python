#melhorando progressão aritmética
razao = 0
cont = 0
termo = 1
while termo != 0:
    if termo == 0:
        print('Fim')
    else:
        termo = int(input('Digite o termo da progressão aritmética: '))
        razao = int(input('Digite a razão da progressão aritmética: '))
        calc = termo
        while cont < 10:
            calc = calc + razao
            cont += 1
            print(calc)
    calc = 0
    cont = 0

    