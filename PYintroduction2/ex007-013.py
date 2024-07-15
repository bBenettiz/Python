#ler 5 n e guardar em lista, mostrar qual o maior e menor valor, e suas posicoes
"""
lst = []
for i in range(5):
    n = int(input(f'Enter your {i+1}° number: '))
    lst.append(n)
    bgst = max(lst)
    smlst = min(lst)
print(f'{bgst} is the biggest number, and its in position number {lst.index(bgst)}')
print(f'{smlst} is the smallest number, and its in position number {lst.index(smlst)}')
"""
#receber varios valores em uma lista, se o numero ja existe, n sera add, exibir os valores em ordem crescente
"""
lst = []
while True:
    n = int(input('Enter your value: '))
    if n in lst:
        r = str(input('Number already added, continue?(y/n)'))
    else:
        lst.append(n)
        r = str(input('Continue?(y/n)'))
    if r in 'Nn':
        break
lst.sort()
print(lst)
"""
#receber 5 n em uma lista, ja na posicao correta, sem uso de sort
"""
lst = []
for i in range(5):
    n = int(input(f'Enter your {i+1}° number: '))
    index = 0
    for j in range(len(lst)):
        if lst[j] < n:
            index = j + 1
        else:
            break
    lst.insert(index, n)
print(lst)
"""
#receber varios n em uma lista, mostrar qtd de n digitados, lista decrescente, se o valor 5 foi digitado e esta ou nao na lista
"""
count = 'y'
lst = []
while count == 'y':
    n = int(input('Enter your value: '))
    lst.append(n)
    count = input('Continue?(y/n)')
print(f'Amount of numbers: {len(lst)}')
lst.sort(reverse=True)
print(lst)
if 5 in lst:
    print(f'Number 5 is in the list, in {lst.index(5)} position')
else:
    print('No number 5 in this list')
"""
#receber varios n em uma lista, criar duas listas, uma apenas com os pares, outra com os impares, mostre as tres listas
"""
count = 'y'
lst = []
evenlst = []
oddlst = []
while count == 'y':
    n = int(input('Enter your value: '))
    lst.append(n)
    count = input('Continue?(y/n)')
for i in lst:
    if i % 2 ==0:
        evenlst.append(i)
    else:
        oddlst.append(i)
print(f'All numbers list: {lst}')
print(f'Even numbers list: {evenlst}')
print(f'Odd numbers list: {oddlst}')
"""
#ler uma expressao que use (), analisar se eles estao fechados na ordem correta
"""
text = input('Enter a mathematical expression: ')
lst = []
for i in range(0, len(text)):
    lst.append(text[i])
if '(' or ')' in lst:
    Ocount = lst.count('(')
    Ccount = lst.count(')')
    if Ocount != Ccount:
        print('There is a parenthesis missing')
    else:
        print('Nothing wrong with the parenthesis')
"""