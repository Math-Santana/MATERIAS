num = int(input("Informe um número inteiro:"))
i=0

while (num!=0):
    
    if (i==0):
        aux = num+1
    
    if (num<aux):
        aux = num

    i = i+1

    num = int(input("Informe um número inteiro:"))

print("O menor valor fornecido foi:",aux)