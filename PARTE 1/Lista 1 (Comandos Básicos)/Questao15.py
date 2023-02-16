aux = 0

num = int(input("Informe um número:"))

for i in range (2,num+1):
    if ((num%i)==0):
        aux=aux+1

if ((aux==1)):
    print("O número",num,"é primo")
else:
    print("O número",num,"não é primo")

#___________Jeito_do_professor______________
#import math
#num = int(input("Número1"))
#raiz = int(math.sqrt(num))
#d=2

#while d<=raiz and num%d!=0:
#   d=d+1

#if d>raiz:
#   print("O número",num,"é primo")
#else:
#    print("O número",num,"não é primo",d,"é um divisor")

