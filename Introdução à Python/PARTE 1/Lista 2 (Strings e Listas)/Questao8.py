'''N=0

while(N>=0):
    N = int(input("Informe um número: "))'''
    
#__________Jeito do professor_____________________________
numeros = []

n = int(input('Número negativo para:'))

while n>=0:
    if n>9 and n<100:
        numeros.append(n)
    n = int(input('Número negativo para:'))

#Para reveter a ordem dos números ou bota assim
numeros.reverse()
print(numeros)

#Ou assim
for i in range (len (numeros) -1,-1,-1):
    print(numeros[i],' ',end='')