F=[0,1]
N=int(input("Informe quantos elementos da série de Fibonacci você deseja: "))

with open ("Fibonacci.txt","w") as arq:
    for i in range(N):
        F.append(F[i]+F[i+1])
        arq.write(str(F[i])+"\n")