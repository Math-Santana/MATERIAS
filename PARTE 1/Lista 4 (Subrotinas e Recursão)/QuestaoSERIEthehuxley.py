import math

def formula(N):
    val=[]
    for n in range (1,N+1):
        val.append(math.factorial(n)/(math.sqrt(2*n+1)))
    val.reverse()
    return val

#Codigo principal
N=int(input())
S=0
val=formula(N)
for i in range(N):
    S=S+val[i]

print("S: {:.12f}".format(S))
for i in range (1,N):
    print("{:.12f}".format(val[i]))