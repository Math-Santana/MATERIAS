num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))

while (num2==0):
    num2 = int(input("Informe o segundo número, de modo que seja diferente de 0:"))

resto = num1%num2

if (resto==0):
    print(num1)

else:
    quadradoresto=resto**2
    print(quadradoresto)