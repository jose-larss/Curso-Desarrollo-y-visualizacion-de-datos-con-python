def complicated_function(x, y):
    print(x,y)
    pass

complicated_function(y = 2, x= 1)


def complicated_function(x, y, z):
    print(x,y)
    pass

complicated_function(1, z = 2, y=3)

def complicated_function(x, y, z):
    print(x,y)
    pass

#complicated_function(z = 2, 1, y = 3) # ERROR

def complicated_function(x, y, z = 10):
    print(x,y)
    pass

complicated_function(1, 3)

#args acepta cualquier numero de positional arguments
def complicated_function(x, y, *args):
    print(x,y, args)
    pass

complicated_function(1, 3, 3, 4, 5, 6, 7, 8, 9)

#args acepta cualquier numero de positional arguments
def complicated_function(*args):
    print(args)
    pass

#incluso si no le pasamos nada, no da error
complicated_function()

lista1 = [1,2,3,4]
lista2 = [1,2,3,4,5,6,7,8]
lista3 = [1,2,3,4]
#args acepta cualquier numero de positional arguments
#kwargs acepta cualquier numero de keyword arguments
def complicated_function(*args, **kwargs):
    print(args, kwargs)
    print(kwargs['s'])
    pass

complicated_function(x = 1, s = 'hello', b = True)

#args acepta cualquier numero de positional arguments
#kwargs acepta cualquier numero de keyword arguments
def complicated_function(*args, **kwargs):
    print(args, kwargs)
    print(args[0])


complicated_function(1,2,3,x = 1, s = 'hello', b = True)

def complicated_function(*args, **kwargs):
    print(args, kwargs)
    print(args[1])


complicated_function(lista1, lista2, lista3,x = 1, s = 'hello', b = True)

def complicated_function(a,b,c = True, d = False):
    print(a,b)

# con * delante descompones los argumentos de la lista en 2 elementos o los que tenga dentro
complicated_function(*[1,2])

def complicated_function(a,b,c = True, d = False):
    print(a,b, c, d)

# con * delante descompones los argumentos de la lista en 2 elementos o los que tenga dentro
complicated_function(*[1,2], **{'c': 'hello', 'd' : 'cool'})