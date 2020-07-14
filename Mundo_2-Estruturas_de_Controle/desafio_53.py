#palindrome

frase = input('Digite uma frase: ').lower()
nova = frase.replace(' ', '')
palin = nova[::-1]
if nova == palin:
    print('É palíndrome')
else:
    print('Não é palíndrome')


    
