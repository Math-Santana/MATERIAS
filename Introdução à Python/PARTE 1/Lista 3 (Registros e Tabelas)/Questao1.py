codigo=2
aux=0
aux2=0
cursos={}

while (codigo>0):
    codigo = int(input("Informe o código do curso:"))
    if(codigo>0):
        nome = input("Digite o nome do curso correspondente ao código informado: ")
        centro = int(input("Informe a que centro esse curso pertence:"))
        while (centro<1):
            codigo = int(input("Informe o código do curso:"))
        cursos[codigo]=(nome,centro)
        print(cursos)

centro = int(input('Digite um centro para buscar os cursos associados: '))
while (centro>0):
    for i in cursos:
        if (cursos[i][1]==centro):
            if(aux2==1):
                print("O(s) curso(s) e código(s) existentes no centro %d, são respectivamente:" %(centro))
                aux=aux+1
            print("curso: %s |codigo: %d" %(cursos[i][0],i))
            aux=aux+1
    if(aux==0):
        print("Nenhum curso encontrado")
    centro = int(input("Informe outro centro:"))

print("Fim de programa")

