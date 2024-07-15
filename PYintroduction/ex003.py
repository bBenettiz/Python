print('showdata')
var = input('Type your data ')
print('Is alpha?')
print(var.isalpha())
print('Is numeric?')
print(var.isnumeric())

if var.isnumeric():
    print('Data type:\n', type(int(var)))
elif var.isalpha():
    print('Data type:\n', type(str(var)))
