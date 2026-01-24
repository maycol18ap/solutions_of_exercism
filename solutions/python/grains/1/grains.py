def square(number):
    '''validacion de numero'''
    if number>0 and number<=64:
        producto=2**(number-1)
        return producto
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    #aqui se cuenta el total de granos de trigos que se obtendra
    return (2**64)-1

#te soy sincero? si sufri un poco me perdi en la compresion de lectura un poco tuve que rebuscar mucho
