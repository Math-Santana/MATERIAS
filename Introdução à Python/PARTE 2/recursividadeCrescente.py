def crescente (N):
    if(len(N)<=1):
        return True
    return N[1]>=N[0] and crescente(N[1:])

N=[1,2,3,4,5]
res=crescente(N)
print(res)

#Jeito_do_professor_____

ascendente 


    