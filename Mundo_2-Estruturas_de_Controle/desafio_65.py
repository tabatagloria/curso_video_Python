n = 0
maior = 0
menor = n
media = 0
cont = 0
calc = 0
opcao = ''
while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = input('Deseja continuar S ou N: ').upper()
    if opcao == 'N':
        print('Fim')
    else:
        calc = calc + n
        cont +=1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = calc / cont
print('A média dos números digitados é {} o maior valor lido foi {} e o menor valor lido foi {}'.format(media, maior, menor))
