aux1 = 1
aux2 = 5
n = -1

num1 = int(input("Informe um valor inteiro:"))

for i in range (0,num1-1):
    n = n  + aux1
    aux1, aux2 = aux2, aux1
    print(i)

print("O valor na posição",num1,"é igual a",n)