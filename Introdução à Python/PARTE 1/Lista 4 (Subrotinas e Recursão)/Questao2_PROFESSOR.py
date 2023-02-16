def inverte (n):
    inv = 0
    while n>0:
        inv = inv*10+(n%10)
        n=n//10

    return inv


num = int(input("Numero: "))
while num<100:
    num = int(input("Invalido. Numero: "))

for i in range(100, num+1):
    if (i==inverte(i)):
        print(i, "é palindromo")
