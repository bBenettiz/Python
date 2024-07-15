#gerar um numero entre 0 e 5, o usuario devera descobrir qual o numero escolhido
"""
import random
print('A number between 0 and 5 will be sorted, then you will try to guess the right number\n')
number = random.randrange(0, 5)
print('You have 3 attempts\n')
guess = int(input('Make your guess: \n'))
for i in range(2):
    if guess == number:
        print('Your guess is correct, the number sorted is: {}'.format(guess))
        exit()
    else:
        print('Not this one, try again')
        guess = int(input('Make your guess: \n'))
print('you lost, the number sorted was: {}'.format(number))
exit()
"""
#ler a velocidade de um carro, se for maior que 80km/h, foi multado no valor de r$7,00 por km ultrapassado
"""
speed = int(input('What was the speed of the car?\n'))
if speed > 80:
    value = (speed - 80)*7
    print('The limit of the road is 80, you were driving at {}'.format(speed))
    print('You have been fined in R${},00'.format(value))
else:
    print('You have not been fined')
"""
#ler um numero, mostrar se é par ou impar
"""
value = int(input('Write a number: \n'))
if value % 2 == 0:
    print('even number')
else:
    print('odd number')
"""
#ler a distancia de uma viagem em km, calcule o preco da passagem(R$0,50 por km para viagens de até 200km e R$0,45 para viagens maiores)
"""
dist = int(input('What is distance of the destiny?\n'))
if dist <= 200:
    value = dist * 0.5
    print('Total value: {}'.format(value))
elif dist > 200:
    value = dist * 0.45
    print('Total value: {}'.format(value))
"""
#ler um ano e mostrar se ele e bissexto
"""
year = int(input('Enter a year to find out if it is a leap year or not: \n'))
if year % 4 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))
"""
#ler tres numeros, mostrar o menor e o maior
"""
num = []
for i in range(3):
    number = int(input(f'Write the {i+1}° number: \n'))
    num.append(number)
if num[0] > num[1] and num[0] > num[2]:
    largest = num[0]
    if num[1] < num[2]:
        smallest = num[1]
    else:
        smallest = num[2]
elif num[1] > num[0] and num[1] > num[2]:
    largest = num[1]
    if num[0] < num[2]:
        smallest = num[0]
    else:
        smallest = num[2]
else:
    largest = num[2]
    if num[1] < num[0]:
        smallest = num[1]
    else:
        smallest = num[0]
print('largest: {}'.format(largest))
print('smallest: {}'.format(smallest))
"""
#ler um salario, se for a cima de 1250, aumento de 10%, para inferiores ou iguais, aumento de 15%
"""
sal = float(input('Enter your salary to check the raise: \n'))
if sal > 1250:
    sal = sal+(sal*0.1)
    print('With the raise, your current salary is: {}'.format(sal))
else:
    sal = sal+(sal*0.15)
    print('With the raise, your current salary is: {}'.format(sal))
"""
#ler o tamanho de tres retas, mostrar se e possivel formar um triangulo com essas medidas
"""
t = []
print('Enter tree straights values to check if its possible to build a triangle')
for i in range(3):
    n = int(input(f'Write the {i+1}° value: \n'))
    t.append(n)
if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
    print('With those values, you can build a triangle')
else:
    print('With those values, you can not build a triangle')
"""
