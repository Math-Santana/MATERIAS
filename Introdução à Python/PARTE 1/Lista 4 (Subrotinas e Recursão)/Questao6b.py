def serieR(n,mul=37,nu=38,de=1):
    if(n<=0):
        res=0
    else:
        res=mul*(nu/de) + serieR(n-1,mul-1,nu-1,de+1)
    return res

num=int(input("Número de termos: "))
res=serieR(num)
print(res)