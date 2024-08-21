velocidade = float(input('Qual sua velocidade?'))
if velocidade <=80:
    print('Ok, sem problemas')
elif velocidade > 80:
    print('Você será multado!!!')
    qtdemulta = velocidade - 80.0
    valormulta = qtdemulta * 7
    print("você pagará R${:.2f}".format(valormulta))
print('Fim do programa')
