nome = input('Informe seu nome completo:')

for i in nome:
    branco=nome.find(" ")
    primNome=nome[:branco]
    print(primNome)

for i in (nome,-1):
    branco=nome.find(" ")
    ultNome=nome[-1:branco]
    print(ultNome)
