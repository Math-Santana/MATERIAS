numerador = 38
denominador = 1
multiplicador = 37
S = 0

N = int(input("Informe o número de vezes a ser somado:"))

for i in range (0,N):
    S = S + multiplicador*(numerador/denominador)
    multiplicador = multiplicador - 1
    numerador = numerador - 1
    denominador = denominador + 1

print("A soma correspondente é de:",S)