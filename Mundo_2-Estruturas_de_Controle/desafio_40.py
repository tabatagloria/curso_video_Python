#análise de nota e média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média {} - REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9: #outra forma de escrever o código: 7 > media >= 5
    print('Média {} - RECUPERAÇÃO'.format(media))
else:
    print('Média {} - APROVADO'.format(media))