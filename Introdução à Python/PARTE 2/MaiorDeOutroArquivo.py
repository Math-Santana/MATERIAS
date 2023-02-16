aux=0

with open ("nums.txt","r") as arquivo:
    for i in arquivo:
        i=int(i)
        if (i>=aux):
            aux = i
    
    print("O maior valor fornecido foi:",aux)