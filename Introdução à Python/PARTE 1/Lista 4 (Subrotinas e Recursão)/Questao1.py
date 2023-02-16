def palindromo (n):
    var=0
    numeros=list(n)
    for i in range(len(numeros)):
        if(int(numeros[i])==4):
            var=var+1
    return var


n = int(input("Informe um numero: "))
while (0<n and 100000>n):  
    n=str(n)
    resultado=palindromo(n)

    print(int(resultado))
    n=int(input("Informe um numero: "))
