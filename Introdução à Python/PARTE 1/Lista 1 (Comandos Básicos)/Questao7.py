soma = 0

lim1 = int(input("Informe um número:"))
lim2 = int(input("Informe outro número:"))

for i in range (lim1,lim2):
    if ((i%2)!=0):
        soma = soma + i

print("A soma dos números inteiros ímpares para o intervalo estabelecido é de:",soma)