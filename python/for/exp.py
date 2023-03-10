base = int(input("Nº 1: "))
exp = int(input("Nº 2: "))
resultado = 0
i=1

if exp != 0:
    for x in range(exp):
        resultado = base**i
        print(base," ^ ",i," = ",resultado)
        exp-=1
        i+=1
else:
    print(base," ^ ",exp," = ",base**exp)