#something that can be looped is called iterable, like a list, a tuple, etc
sellers = ['Marcus', 'Amanda', 'Ale', 'Carol']
sellings = [15, 20, 10, 30]

for i in range(len(sellers)):
    print(sellers[i], end=' ')
    print(sellings[i])
print('\n')
#
#          USING ENUMERATE
# i = position, seller = variable
for i, seller in enumerate(sellers):
    print(seller, end=' ')
    print(sellings[i])
print('\n')
#
#          USING ZIP
#
for seller, selling in zip(sellers, sellings):
    print(seller, selling)