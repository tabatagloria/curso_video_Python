#procurando palavra

nome = str(input('Digite seu nome completo: ')).strip()
pesquisa = 'SILVA' in nome.upper()
print(pesquisa)