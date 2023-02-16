#_____Utilizando__FOR______________________________
soma = 0 

for i in range (50,101):
    
    if ((i%2)==0):
        soma = soma+i

print("A soma dos números inteiros pares é:",soma)

#_____Utilizando__WHILE______________________________
soma = 0 
i = 50

while (i<=100):

    if ((i%2)==0):
        soma = soma + i
    
    i = i+1

print("A soma dos números inteiros pares é:",soma)
