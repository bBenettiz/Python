#dictionaries are like lists and tuples, but they have literal indexes, not only number like lists or tuples, they are identified by {}
#example:

di = {'name':'Bruno', 'age':19, 'lastname':'Benetti'}
print(di['name'])
print(di['age'])
di['height'] = 1.80
print(di['height'])
print(di)
del di['lastname']
print(di.items())
print(di.values())
print(di.keys())

for k, v in di.items():
    print(f'{k}: {v}')


di2 = {'name':'X', 'age':20, 'lastname':'XXXX'}
lst = [di, di2]
print(lst)
print(lst[0]['age'])
print(lst[1]['age'])