aux = 1

i=2


num1 = int(input("Informe um número inteiro positivo:"))
while (num1<1):
    num1 = int(input("Informe um número inteiro positivo:"))

num2 = int(input("Informe um número inteiro positivo:"))
while (num2<1):
    num2 = int(input("Informe um número inteiro positivo:"))

v1=num1
v2=num2

while (i<=num1) or (i<=num2):
    if (((num1%i)==0) or ((num2%i)==0)):
        aux = aux*i
        if ((num1%i)==0):
            num1 = num1/i
        if ((num2%i)==0):
            num2 = num2/i
    else:
        i=i+1
    

print("O MMC para os números",v1,"e",v2,"é de",aux)