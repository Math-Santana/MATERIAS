aux = 0
num = int(input("Informe um número:"))
while (num<1):
    num = int(input("Informe um número inteiro positivo:"))

for i in range (1,num):
    if ((num%i)==0):
        aux=aux+i

if ((num==aux)):
    print("O número",num,"é perfeito")
else:
    print("O número",num,"não é perfeito")