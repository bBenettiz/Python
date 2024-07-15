#crie uma funcao chamada area, que receba as dimensoes de um terreno retangular e mostre a area
"""
def area(length, width):
    print(length*width)
print('AREA CALCULATOR FUNCTION')
length = int(input('Enter the length: '))
width = int(input('Enter the length: '))
print('AREA: ', end='')
area(length, width)
"""
#crie uma funcao escreva, receba texto como parametro e mostre uma msg contendo linhas com o tamanho adaptavel
"""
def escreva(txt):
    print('-'*len(text))
    print(f'{text}')
    print('-' * len(text))
print('TEXT FUNCTION')
text = str(input('Enter the text: '))
escreva(text)
"""
#crie uma funcao contador, receba 3 parametros, incio, fim, e passo, e faca contagem
#de 1 a 10, de 1 em 1
#de 10 a 0, de 2 em 2
#contagem personalizada
"""
def contador(i,f,p):
    for i in range(i, f+1, p):
        print(i)
for i in range(1,11,1):
    print(i, end=' ')
print()
lst = []
for i in range(0, 12, 2):
    lst.append(i)
lst.sort(reverse=True)
for i in lst:
    print(i, end=' ')
print()
i = int(input('Enter the count start: '))
m = int(input('Enter the count end: '))
p = int(input('Enter the count step: '))
contador(i,m,p)
"""
#crie uma funcao maior, que receba x parametros com valores inteiros, analisar todos e dizer qual o maior
"""
from random import randint
def maior(lst):
    print(max(lst))
lst = []
qt = int(input('How many numbers to check?\n'))
for i in range(0, qt):
    lst.append(randint(1,10))
print(lst)
maior(lst)
"""
#crie uma lista num, e duas funcoes, sorteia e somapar, sorteia vai sortear 5 numeros e colocalos em uma lista, somapar
#vai mostrar a soma entre todos os valores pares sorteados.
"""
from random import randint
def sorteia(lst):
    for i in range(5):
        lst.append(randint(1,10))
def somapar(lst):
    num = []
    for i in lst:
        if i % 2 == 0:
            num.append(i)
    print(sum(num))

lst = []
sorteia(lst)
print(lst)
somapar(lst)
"""