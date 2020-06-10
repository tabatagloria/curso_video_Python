#cálculo de preço

valor = float(input('Preço produto: R$'))
print('Forma de Pagamento')
print('1 - À vista (dinheiro/cheque) \n2 - À vista no cartão \n3 - 2x no cartão \n4 - acima de 3x no cartão')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    total = valor - (valor * 0.10)
    print('Total: R${:.2f}'.format(total))
elif opcao == 2:
    total = valor - (valor * 0.05)
    print('Total: R${:.2f}'.format(total))
elif opcao == 3:
    print('Total: {:.2f}'.format(valor))
else:
    total = valor + (valor * 0.20)
    print('Total: R${:.2f}'.format(total))