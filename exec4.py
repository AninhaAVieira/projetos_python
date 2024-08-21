km = float(input('Qual a distancia da viagem?'))
if km > 200.0:
    valorpassagem = km*0.45
elif km <= 200:
    valorpassagem = km*0.50
print('valor da passagem é R${:.2f} '.format(valorpassagem))