var = 'ola bruno tudo bem'
print(len(var), 'caracteres')
print(var)
print(var[0])
print(var[1])
print(var[2])
print(var[4:9])
print(var[:6])
print(var[4:])
print(var[0::2])
print(var.count('o'))
print(var.count('o',0,10))
print(var.find('o',10,))
print(var.find('bruno'))
print('bruno' in var)
print(var.replace('bruno','benetti'))

newVar = var.split()
print(newVar, '\n')
print(newVar[1], '\n')
print('+'.join(newVar))



