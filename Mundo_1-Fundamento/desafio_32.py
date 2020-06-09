#calculo de ano bissexto
from datetime import date #módulo de datas

ano = int(input('Digite um ano ou digite 0 para o ano atual: '))
#importa o ano atual
if ano == 0:
    ano = date.today().year
    
bissexto = ano % 4
if bissexto == 0:
    calc = ano % 100
    if calc != 0:
        print('O ano é bissexto!')
    else:
        print('O ano não é bissexto!')
else:
    calc = ano % 400
    if calc != 0:
        print('O ano não é bissexto!')
    else:
        print('O ano é bissexto!')
