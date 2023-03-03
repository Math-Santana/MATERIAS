#_____Utilizando__FOR______________________________
fatorial = 1

num = int(input("Informe um número inteiro:"))

for i in range (num,1,-1):
    fatorial = fatorial*i

print("O fatorial de", num,"é igual a",fatorial)

#_____Utilizando__WHILE______________________________
fatorial = 1

num = int(input("Informe um número inteiro:"))
i = num

while(i>=1):
    fatorial = fatorial*i
    i = i-1

print("O fatorial de", num,"é igual a",fatorial)