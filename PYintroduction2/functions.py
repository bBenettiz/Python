#Def(Define Function)
#functions are like routines, it helps you with repetitive tasks
#example:
def showline():
    print('-'*10)
showline()
print('Hello Word')
showline()
#you can also create functions with parameters
#example:
print()
def message(msg):
    showline()
    print(msg)
    showline()
message('Message with parameter')
#docstrings works as a documentation of the function, it shows the user the right way to use it
#you can see the docstring with the function help()
#example:
def x(i,f,p):
    """
    :param i: count start
    :param f: count end
    :param p: count step
    :return: no return
    """
    c = i
    while c<= f:
        print(f'{c}', end='')
        c += p #sum the c value + p
    print('Fim')
print()
help(x)
print()
#optional parameters can be declared when you attribute 0 to its value
#example:
def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'{s}')
somar(3,2,5)
somar(2,3)
somar()
print()
def teste(b):
    global a #Using the global variable means that the value that is gonna be used or changed, is the global(out of the function) one
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
teste(a)
print(f'A fora vale {a}')
print()
def returnsomar(a=0,b=0,c=0):
    s = a + b + c
    return s
print(returnsomar(3,2,5))
print(returnsomar(2,3))
print(returnsomar())