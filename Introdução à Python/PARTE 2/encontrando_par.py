def encontrar_numero_par(L):
    for n in L:
        if(n%2==0):
            return n
    raise ValueError("Não tem número par na lista")
        



try:
    print(str(encontrar_numero_par([1,2,3,4,5])))
    print(str(encontrar_numero_par([1,3,4,5])))
    print(str(encontrar_numero_par([1,3,5])))

except ValueError:
    print("Informou uma lista sem números pares")