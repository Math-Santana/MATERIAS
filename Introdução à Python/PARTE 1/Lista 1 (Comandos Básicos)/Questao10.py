
i=1

while (i==1):
    N = int(input("Informe um número"))

    while (N<1 or N>3900):
        N = int(input("Informe um número"))

    milhar = N//1000
    centena = (N%1000)//100
    dezena = ((N%1000)%100)//10
    unidade = ((N%1000)%100)%10

    for n in range (milhar):
        print("M",end="")

    if (centena>=5):
        if (centena==9):
            print("CM",end="")
        else:
            print("D",end="")
            centena=centena-5
    if (0<centena<5):
        if (centena==4):
            print("CD",end="")
        else:
            for n in range (centena):
                print("C",end="")

    if (dezena>=5):
        if (dezena==9):
            print("XC",end="")
        else:
            print("L",end="")
            dezena=dezena-5
    if (0<dezena<5):
        if (dezena==4):
            print("XL",end="")
        else:
            for n in range (dezena):
                print("X",end="")


    if (unidade>=5):
        if (unidade==9):
            print("IX",end="")
        else:
            print("V",end="")
            unidade=unidade-5
    if (0<unidade<5):
        if (unidade==4):
            print("IV",end="")
        else:
            for n in range (unidade):
                print("I",end="")

    print("")
    i = int(input("Deseja informar um novo número? Digite 1 para SIM e 0 para NÃO"))


