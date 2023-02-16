
i=0
while (i<3):
    num1 = float(input("Informe um número:"))
    
    if (i==0):
        aux = num1+1
    
    if (num1<aux):
        aux = num1
    
    i = i + 1

print("O menor valor fornecido foi:",aux)