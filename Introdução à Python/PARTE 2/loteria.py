import random

def numeros_loteria(qtde,min,max):
    numeros=[]
    for i in range(0,qtde):
        numero=random.randrange(min,max)
        numeros.append(numero)

    return numeros


for numero in numeros_loteria(6,1,60):
    print (numero)