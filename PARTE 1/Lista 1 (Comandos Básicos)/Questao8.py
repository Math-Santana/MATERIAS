lim1 = int(input("Informe a temperatura mínima:"))
lim2 = int(input("Informe a temperatura máxima:"))

print("   °F   |   °C   ")

for F in range (lim1,lim2):
    C=(F-32)*(5/9)
    print("   ",F,"   |   ",C,"   ")