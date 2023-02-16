def serieR (aux,n,nu=2,de=500):
    if(aux%2!=0):
        nu=2
    else:
        nu=-5
    
    if(aux<=n):
        print(n)
        print("aux:",aux)
        res = nu/de + serieR(aux+1,n,nu,de-10)
    else:
        res=0

    
    return res

num = int(input("Número de termos: "))
res = serieR(1,num)
print(res)