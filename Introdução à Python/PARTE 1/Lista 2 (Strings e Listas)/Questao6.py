'''vetor0=[]
vetor1=[]
vetor2=[]

N = int(input("Informe o tamanho do vetor:"))

for i in range(N):
    aux=int(input("Informe um valor:"))
    vetor0.append(aux)

    if(aux%2==0 and aux!=0):
        vetor1.append(aux)
    if(aux%2!=0):
        vetor2.append(aux)

print("O vetor informado foi",vetor0)
print("Os números pares do vetor informado são:",vetor1)
print("Os números ímpares do vetor informado são:",vetor2)'''

#___________Jeito do professor_______________________
n = int(input('Tamanaho: '))

#Comandos para caso n seja menor que 1, pois assim não haveria tamanho de vetor
while n<1:
    n = int(input('Inválido. Tamanho:'))

#Aplicando o tamanho aos vetores, justamente para reservar um tamanho específico na memória
v1 = [0]*n
par = [0]*n
imp = [0]*n

qp = qi = 0

for i in range(n):
    v1[i] = int(input('V1 elemento' + str(i) + ': '))
    if v1[i]%2==0 :
        par[qp] = v1[i]
        qp=qp+1
    else:
        imp[qi]=v1[i]
        qi=qi+1

par=par[:qp]
imp=imp[:qi]

print('Lidos =',v1)
print('Pares =',par)
print('Impares =',imp)
