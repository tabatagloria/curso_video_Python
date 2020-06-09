#multa acima do limite de velocidade

velocidade = float(input('Digite a velocidade do veículo: ')) #solicita a velocidade do veículo pelo usuário

#caso a velocidade seja superior ao permitido calcula a multa para o usuário
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você estava dirigindo a {}km/h você foi multado em R${:.2f}'.format(velocidade, multa))

#caso contrário printa mensagem de ba viagem
else:
    print('Boa viagem! Dirija com segurança!')