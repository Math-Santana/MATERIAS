#__________Jeito do professor______________

tab = {}
n = idMax = idMin = qtd = qtd2 = 0

cpf = int(input('CPF: '))
#Para na primeira vez colocar um cpf válido pelo menos
while (cpf<=0):
    cpf = int(input("Digite um CPF válido: "))

while (cpf>0 and qtd<200):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    #Comando para solicitar uma nova idade caso a anterior seja inválida, negativa, por exemplo
    while(idade<0):
        idade = int(input("Inválida. Idade: "))
    #Alocando o nome e a idade no dicionário, de acordo com o CPF
    tab[cpf] = (nome, idade)
    #Contagem da quantidade de alunos
    qtd = qtd + 1
    cpf = int(input('CPF: '))

#Não seria necessário, só uma sofisticação
if (cpf>0):
    print("leitura interrompida, último CPF desprezado")

n = int(input("Quantidade de intervalos: "))
while n<=0:
    n = int(input("Inválido. Quantidade de intervalos: "))

#Parte da análise dos alunos que se enquadram no intervalo de idade a ser estabelecido
for i in range (n):
    #Leitura da idade mínima
    idMin = int(input("Idade mínima: "))
    while (idMin<0):
        idMin = int(input("Inválida. Idade mínima: "))
    #leitura da idade máxima
    idMax = int(input("Idade máxima: "))
    #Só realizará a análise se a idade máxima for maior que a mínima
    if(idMax>=idMin):
        #Variável par a contagem de quantos alunos estão dentro do intervalo de idade estabelecido
        qtd2 = 0
        for ch in tab:
            if( tab[ch][1]>=idMin and tab[ch][1]<=idMax):
                print(ch, tab[ch][0], tab[ch][1])
                qtd2 = qtd2 + 1
        print("Quantidade de alunos =",qtd2)
    else:
        print("Intervalo inválido, desprezado")
