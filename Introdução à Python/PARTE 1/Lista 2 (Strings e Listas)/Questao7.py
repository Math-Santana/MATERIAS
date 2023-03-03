notas=[]
soma=0.0

N = int(input("Quantos alunos terão sua nota cadastrada? "))

for i in range(N):
    aux=int(input("Informe a nota:"))
    notas.append(aux)

for i in range(N):
    soma=soma+notas[i]

media=soma/N

print("A média das notas fornecidas é igual a",media)
print("As notas maiores que as médias foram:")

for i in range (N):
    if (notas[i]>media):
        print("->",notas[i])
