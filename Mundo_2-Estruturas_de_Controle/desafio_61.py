termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
cont = 0
calc = termo
while cont < 10:
    calc = calc + razao
    cont += 1
    print(calc)
