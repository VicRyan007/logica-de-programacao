num = int(input("Nº 1: "))
num1 = int(input("Nº 2: "))

totalPares = 0

while num<num1:
    if num%2==0:
        totalPares+=1
    num+=1
    

print("Quantidade de números pares: ",totalPares)