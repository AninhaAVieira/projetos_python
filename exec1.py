import random
x = int(random.randint(0,5))
n = int(input('Tente adivinhar qual número foi sorteado: '))

if n==x:
    print('Você acertou!!!')
else:
    print('Você errou')
print('Número = {}'.format(x))