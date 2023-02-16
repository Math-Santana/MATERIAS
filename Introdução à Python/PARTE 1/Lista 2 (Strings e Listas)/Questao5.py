"""vetor1 = []
vetor2 = []
soma=[]

N = int(input("Informe o tamanho do vetor:"))

for i in range(N):
    aux=int(input("Informe um valor"))
    vetor1.append(aux)
print("O primeiro vetor é igual a",vetor1)

for i in range(N):
    aux=int(input("Informe um valor"))
    vetor2.append(aux)
print("O segundo vetor é igual a",vetor2)

for i in range (N):
    adicao=vetor1[i]+vetor2[i]
    soma.append(adicao)
print("A soma dos vetores é igual a",soma)"""


#__________Jeito do professor_____________________________
n = int(input('Tamanaho: '))

#Comandos para caso n seja menor que 1, pois assim não haveria tamanho de vetor
while n<1:
    n = int(input('Inválido. Tamanho:'))

#Aplicando o tamanho aos vetores, justamente para reservar um tamanho específico na memória
v1 = [0]*n
v2 = [0]*n
vres = [0]*n

for i in range(n):
    v1[i] = int(input('V1 elemento' + str(i) + ': '))

for i in range(n):
    v2[i] = int(input('V2 elemento' + str(i) + ': '))
    vres[i]=v1[i]+v2[i]

print('V1 =',v1)
print('V2 =',v2)
print('Soma =',vres)
