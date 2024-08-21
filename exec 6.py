n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
n3 = int(input('Digite o ultimo numero '))
maior = n1
if n2>maior:
    maior = n2
if n3>maior:
    maior = n3
menor = n1
if n2<menor:
    menor = n2
if n3<menor:
    menor = n3
print(f'maior {maior}')
print(f'menor {menor}')