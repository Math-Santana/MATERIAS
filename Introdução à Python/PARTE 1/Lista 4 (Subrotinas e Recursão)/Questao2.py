def palindromo (n):
    aux=0
    numeros=list(n)
    NI=list(n)
    NI.reverse()
    for i in range(len(numeros)):
        if(numeros[i]==NI[i]):
            aux=aux+1
    if(aux==len(numeros)):
        saida=n
    else:
        saida="O número informado não é um palíndromo"
    return saida


n=int(input("Informe um numero: "))
while (n<100 or n>5000):
    n=int(input("Inválido. Informe um número: "))
n=str(n)
resultado=palindromo(n)

print(resultado)
