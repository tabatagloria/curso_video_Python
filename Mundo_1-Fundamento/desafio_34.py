#aumento salarial conforme valor do salário

salario = float(input('Digite o valor do salário: R$'))
if salario > 1250.00:
    aumento = (salario * 0.1) + salario
    print('O valor do salário com aumento é: R${:.2f}'.format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print('O valor do salário  com aumento é: R${:.2f}'.format(aumento))