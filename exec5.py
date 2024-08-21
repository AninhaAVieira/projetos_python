ano = int(input('Informe o ano que deseja saber se é ou não bissexto: '))
if ano % 4 == 0:
    if ano % 400 == 0:
        print('Ano bissexto')
    else:
        if ano % 100 == 0:
            print('Não é bissexto')
        else:
            print('É bissexto')
else:
    print('Não é bissexto')
    print('Fim dos testes ')