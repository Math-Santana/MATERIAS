#_______Utilizando__FOR___________
numerador = 1
denominador = 1
S = 0

N = int(input("Informe o número de vezes a ser somado:"))

for i in range (0,N):
    S = S + (numerador/denominador)
    numerador = numerador + 2
    denominador = denominador + 1

print("A soma correspondente é de:",S)

#_______Utilizando__WHILE___________
numerador = 1
denominador = 1
S = 0
i = 0
N = int(input("Informe o número de vezes a ser somado:"))

while (i<N):
    S = S + (numerador/denominador)
    numerador = numerador + 2
    denominador = denominador + 1
    i=i+1

print("A soma correspondente é de:",S)