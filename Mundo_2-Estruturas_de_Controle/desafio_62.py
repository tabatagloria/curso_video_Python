#melhorando progressão aritmética
termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
cont = 0
calc = termo
add = 10
total = 0
while add != 0:
    total += add    
    while cont < total:
        calc += razao
        cont += 1
        print('{} - > '.format(calc), end='')
    add = int(input('\nQuantos termos você quer mostrar a mais: '))
print('Fim do programa')
    