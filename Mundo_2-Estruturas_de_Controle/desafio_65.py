#média, maior e menor
n = maior = menor = media = cont = calc = 0
opcao = ''
while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = input('Deseja continuar S ou N: ').upper().strip()[0]
    if opcao == 'N':
        print('Fim')
    else:
        calc = calc + n
        cont +=1
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
media = calc / cont
print('A média dos números digitados é {} o maior valor lido foi {} e o menor valor lido foi {}'.format(media, maior, menor))
