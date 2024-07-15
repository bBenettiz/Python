#Ler um numero pelo teclado e mostrar sua porcao inteira ex(6.127 = 6)
"""
import math
value = float(input('Type your decimal number'))
print('The integer part of your number is {}'.format(math.trunc(value)))
"""
#Ler o comprimento do cateto oposto e do adjacente de um triangulo ret, mostre a hipotenusa
"""
import math
OpL = float(input('type the size of the opposite cathetus: \n'))
AdL = float(input('type the size of the adjacent cathetus: \n'))
res = OpL**2 + AdL**2
hip = math.sqrt(res)
print('The hypotenuse length is: {:.2f}'.format(hip))
"""
#Ler um angulo qualquer e mostrar seu sen, cos e tan
"""
import math
value = float(input('type the value of the angle: \n'))
print('The angle´s sin: {}, cos: {}, tan: {}'.format(math.sin(value), math.cos(value), math.tan(value)))
"""
#Ler nomes de alunos e sortear um nome
"""
import random
size = int(input('How many names to sort? \n'))
names = []
for i in range(size):
    value = input(str(i+1) + '° name \n')
    names.append(value)
print('The chosen name is: {}'.format(random.choice(names)))
"""
#Ler nomes de alunos e sortear a ordem desses nomes(aleatoria)
"""
import random
size = int(input('How many names to random order? \n'))
names = []
for i in range(size):
    value = input(str(i+1) + '° name \n')
    names.append(value)
random.shuffle(names)
print(names)
"""
#Abra e reproduza um arquivo mp3
"""
import os
file = 'D:/ContentCreator/funk.mp3'
os.system(file)
"""