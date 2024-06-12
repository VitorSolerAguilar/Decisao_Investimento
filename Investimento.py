risco = input('Coloque a aceitação de risco: ')

if risco != 'BX' and risco != 'AL':
    print('Opcao invalida!')
else:
    valor = float(input('Digite o valor do investiento: '))
    if risco == 'BX':
        if valor < 1000:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'

print(f'Voce deve investir em {tipo}')