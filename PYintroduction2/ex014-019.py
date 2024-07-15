#ler nome e peso de varias pessoas, mostre qtd de pessoas cadastradas, lista com as mais pesadas e com as mais leves
"""
person = []
allperson = []
while True:
    person.append(str(input('Enter the person´s name: ')))
    person.append(float(input('Enter the person´s weight: ')))
#the first person will have both the heaviest and the lightest weight, so thats the value attributed to maior and menor
#then at the first else conditional, its checked if the current entered weight is heavier or lower than the first one
#for example, first enter: 10, maior=10, menor=10, this value is add to allperson[] and with person.clear(), its removed
#from person, but maior keeps the value 10, then the loop starts again, second enter: 20, the first condition its skipped
#since len(allperson) != 0, as the person list was cleared, now person[1], is now equals to 20, and then the comparission
#is made, if 20 > 10, maior is now equals 20.
    if len(allperson) == 0:
        maior = menor = person[1]
    else:
        if person[1] > maior:
            maior = person[1]
        if person[1] < menor:
            menor = person[1]
    allperson.append(person[:])
    person.clear()
    loop = str(input('Continue?[Y/N]'))
    if loop in 'Nn':
        break
print(f'Persons registered: {len(allperson)}')
print(f'The heaviest weight is {maior}, from: ', end='')
for i in allperson:
    if i[1] == maior:
        print(f'{i[0]}', end=' ')
print()
print(f'The lightest weight is {menor}, from: ', end='')
for i in allperson:
    if i[1] == menor:
        print(f'{i[0]}', end=' ')
"""
#ler 7 valores numericos em uma lista unica que mantenha separado os pares dos impares, mostre eles em ordem crescente
"""
lst = [[], []]

for i in range(7):
    num = int(input(f'Enter de {i +1}° number: '))
    if num % 2 == 0:
        lst[0].append(num)
    else:
        lst[1].append(num)

print(lst)
lst[0].sort()
lst[1].sort()
print(lst[0])
print(lst[1])
"""
#Crie uma matriz 3x3 e preencha com valores do teclado, mostre a matriz
"""
matrix = [[], [], []]
for i in range(3):
    for x in range(3):
        num = int(input(f'Enter the {i+1}° number at position {[i, x]}: '))
        matrix[i].append(num)
for i in range(3):
    for x in range(3):
        print(f'[{matrix[i][x]:^5}]', end='')
    print()
"""
#Utilize o anterior, mostre a soma dos valores pares, a soma dos valores da terceira coluna, o maior valor da segunda linha
"""
matrix = [[], [], []]
lstsoma = []
for i in range(3):
    for x in range(3):
        num = int(input(f'Enter a number at position {[i, x]}: '))
        matrix[i].append(num)
        if num % 2 == 0:
            lstsoma.append(num)
for i in range(3):
    for x in range(3):
        print(f'[{matrix[i][x]:^5}]', end='')
    print()
evensum = sum(lstsoma)
print(f'Even numbers sum: {evensum}')
lstsoma.clear()
for i in range(len(matrix)):
    lstsoma.append(matrix[i][2])
tdcsum = sum(lstsoma)
print(f'Third column sum: {tdcsum}')
print(f'Biggest second line´s value: {max(matrix[1][:])}')
"""
#crie palpites para megasena, perguntar qtd de jogos que serao gerados, sortear 6n de 1 a 60 para cada jogo
"""
import random
lst = []
count = int(input('How many games you wish? \n'))
for i in range(0, count):
    game = []
    for i in range(6):
        game.append(random.randint(1, 60))
    lst.append(game)
for i in range(len(lst)):
    print(f'Your {i+1}° game is: {lst[i]}')
    """
#ler nome e duas notas de n alunos, guarde em uma lista composta, mostre um boletim contendo a media de cada um e permita
#que o usuario possa mostrar as notas de cada aluno individualmente]
"""
stud = []
gen = []
while True:
    stud.append(str(input('Enter the student´s name: ')))
    stud.append(float(input(f'Enter the student´s 1° grade: ')))
    stud.append(float(input(f'Enter the student´s 2° grade: ')))
    gen.append(stud[:])
    count = str(input('Continue?[y/n] '))
    if count in 'Nn':
        break
    else:
        stud.clear()
print('-'*42)
print(' '*11, 'Student´s scores')
print('-'*42)
print('Name', ' '*3, '1° Score', ' '*3, '2° Score', ' '*3, 'Average')
for i in range(len(gen)):
    src1 = gen[i][1]
    src2 = gen[i][2]
    print(f'{gen[i][0]:<11}', end='')
    print(f'{gen[i][1]:<13}', end='')
    print(f'{gen[i][2]:<13}', end='')
    print((src1+src2)/2)
print()
while True:
    chk = str(input('Enter the student name: '))
    chk.lower()
    print('Name', ' '*3, '1° Score', ' '*3, '2° Score', ' '*3, 'Average')
    for i in range(len(gen)):
        if chk in gen[i][0]:
            src1 = gen[i][1]
            src2 = gen[i][2]
            print(gen[i][0], end=' ' * 11)
            print(gen[i][1], end=' ' * 12)
            print(gen[i][2], end=' ' * 10)
            print((src1 + src2) / 2)
    print()
    lp = str(input('Check another student?[y/n]: '))
    if lp in 'Nn':
        break
"""