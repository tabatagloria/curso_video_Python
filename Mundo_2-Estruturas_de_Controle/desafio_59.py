n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        soma = n1 + n2
        print('A soma dos valores é: {}'.format(soma))
    elif menu == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos valores é: {}'.format(multiplicar))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            print("O valores são iguais")
        else:
            maior = n2
        print('O valor maior é: {}'.format(maior))
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Fim')

    