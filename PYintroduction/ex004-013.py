#ler um numero, mostrar seu antecessor e sucessor
"""
num = int(input('Type your number \n'))
print('Predecessor: {}'.format(num-1))
print('Sucessor: {}'.format(num+1))
"""

#ler um numero, mostrar seu dobro, triplo e raiz quadrada(**1/2)
"""
import math (importa tudo da biblioteca)
from math import sqrt (importa somente sqrt)
num = int(input('Type your number \n'))
print('Double: {}'.format(num*2))
print('Square root: {}'.format(num**(1/2)))
print('Square root(import math): {}'.format(math.sqrt(num)))
"""

#ler duas notas, mostrar a media
"""
m1 = float(input('Type your first score'))
m2 = float(input('Type your second score'))
print('Your average is: {}'.format((m1+m2)/2))
"""

#ler um valor em metros, converter em centimetros e milimetros
"""
m = float(input('Type the value in meters \n'))
print('Value in centimeters: {}'.format(int(m*100)))
print('Value in millimeters: {}'.format(int(m*1000)))
"""

#ler um numero, mostrar sua tabuada
"""
number = int(input('Type the number which you want to see the multiplication table: \n'))
i=0
x=11
for i in range(x):
print(number,'x',i,'= {}'.format(number*i),'\n')
"""

#ler quanto dinheiro tem na carteira, e quantos dolares ela pode comprar  $1 = R$3,27
"""
value = float(input('Type your balance in R$: \n'))
dol = 3.27
if value<dol:
    print('Your balance of {}'.format(value), 'is less than $1 dolar')
    exit()
print('With your balance of R${}'.format(value), 'you can buy ${}'.format(value/dol))
"""

#ler a largura e altura em metros, mostrar sua area e qtd de tinta para pintar ela, 1L = 2m²
"""
height = float(input('Type the wall height in meters: \n'))
width = float(input('Type the wall width in meters: \n'))
area = height*width
print('Wall area: {}²'.format(area))
print('Amount of paint needed: {}L'.format(area/2))
"""

#ler um preco, mostrar seu novo valor com 5% de desconto
"""
value = float(input('Type the value to apply the discount: \n'))
newvalue = value*0.05
print('New value with the discount applied: {}'.format(value - newvalue))
"""

#ler o salario, mostrar seu novo valor com 15% de aumento
"""
value = float(input('Type your salary to apply the 15% raise: \n'))
newvalue = value*0.15
print('New value with the raise applied: {}'.format(value + newvalue))
"""