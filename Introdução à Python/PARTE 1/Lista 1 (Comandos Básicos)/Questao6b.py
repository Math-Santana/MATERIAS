numerador1 = 2
numerador2 = -5
denominador = 500
S = 0

N = int(input("Informe o número de vezes a ser somado:"))

#Para caso coloque um valor menor que 1 ou maior que 50, já que vai acabar fazendo uma divisão por 0.
while N<1 or N>50:
    N = int(input("Informe o número de vezes a ser somado:"))

for i in range (0,N): #Aqui o professor colocou for i in range (1,N+1)
    S = S + (numerador1/denominador)
    numerador1, numerador2 = numerador2, numerador1
    denominador = denominador -10

print("A soma correspondente é de:",S)