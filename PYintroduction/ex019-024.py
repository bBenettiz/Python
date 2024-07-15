# Ler o nome completo de uma pessoa, mostrar todas as letras maiusculas, todas minusculas, qtd de letras sem contar espaco, qtd de letras no primeiro nome
"""
name = input('Write your whole name: \n')
print('Uppercase: ', name.upper())
print('Lowercase: ', name.lower())
print('Characters amount, without space: ', len(name.replace(' ', '')))
firstname = name.split()
print('First name: ', firstname[0])
"""
# ler um n de 0 a 9999, mostre cada um dos digitos separados, unidade:x dezena:y centena:z milhar:w
"""
number = int(input('Choose a number between 0 and 9999: \n'))
while number < 0 or number > 9999:
    print('That number is not between 0 and 9999')
    number = int(input('Choose a number between 0 and 9999: \n'))
newnumber = str(number)
count = len(newnumber)
unit = ['thousand', 'hundreds', 'tens', 'units']
for i in range(count):
    print('{}:'.format(unit[i]), '{}'.format(newnumber[i]))
"""
# ler o nome de uma cidade, mostrar se comeca com a palavra santo
"""
name = input('Write the name of a city: \n')
firstname = name.split()
if firstname[0] == 'santo':
    print('The city´s name starts with Santo')
else:
    print('The city´s name doesnt starts with Santo')
"""
# ler um nome, mostrar se tem silva
"""
var = input('Write a name: \n')
name = var.title()
if ('Silva' in name) == True:
    print('The name silva is in the name')
else:
    print('The name silva is not in the name')
"""
# ler uma frase, mostre quantas vezes a letra A aparece, qual a posicao da primeira e ultima aparicao
"""
var = input('Write something that contains the letter "A": \n')
text = var.lower()
amount = text.count('a')
print('amount: ', amount)
print('first apparition: ', text.find('a'))
print('last apparition: ', text.rfind('a'))
"""
# ler o nome completo, mostrar o primeiro e o ultimo nome
"""
var = input('Write a complete name: \n')
text = var.split()
print('first name: ', text[0])
print('last name: ', text[-1])
"""