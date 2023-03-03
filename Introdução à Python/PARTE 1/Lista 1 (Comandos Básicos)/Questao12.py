soma = 0.0
i = 0

num = float(input("Informe um número:"))

while(num>=0):
    soma=soma+num
    i=i+1
    num = float(input("Informe um número:"))

media=soma/i
print("A média aritmética dos números somados é de",media)