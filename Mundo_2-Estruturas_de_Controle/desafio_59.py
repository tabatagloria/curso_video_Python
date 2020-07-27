#menu de opções
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        soma = n1 + n2
        print('A soma dos valores é: {}\n'.format(soma))
    elif menu == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos valores é: {}\n'.format(multiplicar))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            print("O valores são iguais\n")
        else:
            maior = n2
        print('O valor maior é: {}\n'.format(maior))
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Fim')
    else:
        print('Opção Inválida! Escolha uma opção:')

    