#calculo de desconto de um produto

preco = float(input('Preço: R$'))
desconto = preco - (preco * 0.05)
print('Novo preço: {:.2f}'.format(desconto))