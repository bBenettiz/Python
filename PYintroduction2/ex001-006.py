#crie uma tupla com 0 a 20 escritos por extenso, ler um numero e exibilo por extenso
"""
n = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
number = int(input('Enter a number between 1 and 20: \n'))
value = n[number-1]
print(value)
"""
#crie uma tupla com 20 times, mostre os 5 primeiros colocados, os 4 ultimos, em ordem alfabetica, qual a posicao to time chapecoense
"""
times = ('América-MG', 'Atlético-MG', 'Athletico-PR', 'Bahia', 'Botafogo', 'Bragantino', 'Corinthians', 'Coritiba',
         'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
         'Santos', 'São Paulo', 'Vasco da Gama')
print('Top 5 equips: {}'.format(times[0:5]))
print('Top 4 last equips: {}'.format(times[16:]))
print('Alphabetical order: {}'.format(sorted(times)))
print('Corinthians´s position: {}'.format(times.index('Corinthians')))
"""
#gerar 5 n aleatorios em uma tupla, mostre a listagem de n e indique o menor e o maior valor
"""
import random
lst = []
for i in range(5):
    number = random.randrange(1, 6)
    lst.append(number)
tu = (lst)
print('Random tuple: ', tu)
print('Largest value: ', max(tu))
print('Smallest value: ', min(tu))
"""
#ler 4 valores em uma tupla, mostrar quantas x o 9 apareceu, posicao do primeiro valor 3, n pares
"""
import random
number = random.sample(range(1, 100), 4)
tu = tuple(number)
tustr = str(number)
print(tu)
print('The number 9 appears {} times'.format(tustr.count('9')))
try:
    print('First number 3 appearance: {}'.format(tustr.index('3')))
except ValueError:
    print('No number 3 in this tuple')
for i in tu:
    if i % 2 == 0:
        print('Even numbers: ', i)
"""
#tupla com nomes de produtos e seus precos, mostrar a listagem de precos em forma tabular
"""
prod = ('Camiseta', 50, 'Calça Jeans', 120, 'Tênis Esportivo', 200, 'Relógio', 150, 'Boné', 40, 'Jaqueta', 180,
        'Mochila', 90, 'Óculos de Sol', 250, 'Carteira', 70, 'Fone de Ouvido', 100)
print('-'*30)
print('LISTAGEM DE PRECOS')
print('-'*30)

for i in range(0, len(prod), 2):
        name = prod[i]
        price = prod[i+1]
        print(f'{name:.<25}', price)
"""
#tupla com palavras, mostrar as vogais de cada palavra
"""
times = ('America-MG', 'Atletico-MG', 'Athletico-PR', 'Bahia', 'Botafogo', 'Bragantino', 'Corinthians', 'Coritiba',
         'Cruzeiro', 'Cuiaba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goias', 'Gremio', 'Internacional', 'Palmeiras',
         'Santos', 'Sao Paulo', 'Vasco da Gama')
for i in times:
    print(f'\n{i}, vocals in this word: ', end='')
    for vocals in i:
        if vocals.lower() in 'aeiou':
            print(f'{vocals}', end=' ')
"""


