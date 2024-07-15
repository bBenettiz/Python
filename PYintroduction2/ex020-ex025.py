#ler nome e media, guardando a situacao(<7 reprovado, >7 aprovado) em um dict, mostrar tudo
"""
lst = []
while True:
    name = str(input('Enter a name: '))
    avg = float(input('Enter the average: '))
    if avg < 7:
        sit = 'Reproved'
    else:
        sit = 'Approved'
    di = {'name': name, 'average': avg, 'situation':sit}
    lst.append(di)
    lp = str(input('Continue?[y/n] '))
    if lp in 'Nn':
        break
for i in range(0,len(lst)):
    print(lst[i])
"""


#4 jogadores joguem um dado e tenham resultados aleatorios, guarde em um dict, coloque em ordem, o vencedor tirou o maior num
"""
from random import randint
from time import sleep
from operator import itemgetter
di = {'player 1': randint(0, 6),
      'player 2': randint(0, 6),
      'player 3': randint(0, 6),
      'player 4': randint(0, 6)}
rank = {}
for k, i in di.items():
    print(k, i)
    sleep(0.4)
print()
print('Ordered:')
rank = dict(sorted(di.items(), key=itemgetter(1), reverse=True))#itemgetter IMPORTANTE
for k, i in rank.items():
    print(k, f'with number {i}')
    sleep(0.4)
"""
#ler nome, ano de nasc, carteira de trab, e guarde com a idade(nao a data de nasc), se a carteira for diferente de 0,
#o dict tambem recebera o ano de contratacao e o salario, calcule e acrescente, alem da idade, com quantos anos a pessoa
#vai se aposentar(35 anos de contribuicao)
"""
from datetime import date
di = {}
while True:
    di['name'] = str(input('Enter your name: '))
    dt = int(input('Enter your birth date: '))
    di['age'] = date.today().year - dt
    CkCt = str(input('Do you have CTPS? [Y/N]:\n'))
    if CkCt in 'Yy':
        di['year'] = str(input('Enter the year of hire: '))
        di['salary'] = float(input('Enter your salary: '))
        print()
        if date.today().year - int(di['year']) < 35:
            print(f'You can not retire, {-1 * (date.today().year - int(di['year']) - 35)} more years to retire')
            print(f'You can retire at the age of {(-1 * (date.today().year - int(di['year']) - 35)) + di['age']}')
        else:
            print('You can already retire')
    print()
    lp = str(input('Use again?[Y/N] '))
    if lp in 'Nn':
        break
"""
#gerencie o aproveitamento de um jogador de futebol, ler nome e qtd de partidas jogadas, depois qtd de gols em cada partida
#guardar em um dict com o total de gols
"""
di = {}
goals = []
while True:
    di['name'] = str(input('Enter the player name: '))
    di['matches'] = int(input('Enter the number of matches: '))
    for i in range(0, di['matches']):
        goals.append(int(input(f'Enter the amount of goals in the {i+1}° match: ')))
    tgoals = sum(goals)
    di['goals'] = goals
    di['total goals'] = tgoals
    print()
    for k, v in di.items():
        print(f'{k}: {v}')
    print()
    print(f'The player {di['name']} played {di['matches']} matches')
    for i in range(len(goals)):
        print(f'goals in the {i+1} match: {goals[i]}')
    print()
    lp = str(input('Use again?[Y/N] '))
    if lp in 'Nn':
        break
"""
#ler nome, sexo e idade de x pessoas, em um dict e guardar em uma lista, mostre n de pessoas cadastradas, media de idade
#do grupo, lista com todas as mulheres, lista com pessoas com idade acima da media
"""
lst = []
lstwm = []
age = []
abavg = []
while True:
    di = {}
    di['name'] = (str(input('Enter the name: ')))
    sx = str(input('Sex?[M/F]: ')).lower()
    if sx in 'm':
        sx = 'male'
    else:
        sx = 'female'
    di['sex'] = sx
    di['age'] = (int(input('Enter the age: ')))
    age.append(di['age'])
    lst.append(di)
    lp = str(input('Continue?[y/n] '))
    if lp in 'Nn':
        break
for i in range(len(lst)):
    if lst[i]['sex'] == 'female':
        lstwm.append(lst[i])
avg = int(sum(age)/len(age))
for i in range(len(lst)):
    if lst[i]['age'] > avg:
        abavg.append(lst[i])
print()
print(f'TOTAL PEOPLE REGISTERED: {len(lst)}')
print(f'AGE AVERAGE: {avg}')
print(f'WOMEN REGISTERED: {len(lstwm)}')
for i in range(len(lstwm)):
    print(f'NAME: {lstwm[i]['name']}')
print(f'PEOPLE ABOVE THE AGE AVERAGE: {len(abavg)}')
for i in range(len(abavg)):
    print(f'NAME: {abavg[i]['name']}')
print()
"""
#aprimore o desafio do futebol, para que ele funcione com x jogadores, incluindo um sistema de vizualizacao de detalhes
#do aproveitamento de cada jogador.
"""
lst = []
while True:
    di = {}
    di['name'] = str(input('Enter the player name: ')).title()
    di['matches'] = int(input('Enter the number of matches: '))
    goals = []
    for i in range(0, di['matches']):
        goals.append(int(input(f'Enter the amount of goals in the {i+1}° match: ')))
    tgoals = sum(goals)
    di['goals'] = goals
    di['total goals'] = tgoals
    lst.append(di)
    lp = str(input('Register other player?[Y/N] '))
    if lp in 'Nn':
        break
print()
print('PLAYER STATS')
for i in range(len(lst)):
    print(f'NAME: {lst[i]['name']}  MATCHES: {lst[i]['matches']}')
print()
ck = str(input('Check more info?[Y/N]: '))
while True:
    if ck in 'Yy':
        player = str(input('Enter the player name: ')).title()
        for i in range(len(lst)):
            if lst[i]['name'] == player:
                print(f'NAME: {lst[i]['name']} MATCHES: {lst[i]['matches']} GOALS: {lst[i]['goals']} TOTAL GOALS: {lst[i]['total goals']}')
                print()
        cklp = str(input('Check other player?[Y/N]: '))
        if cklp in 'Nn':
            break
    else:
        exit()
"""
