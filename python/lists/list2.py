pares= [] 
impares= [] 
for i in range(10):
    n = int(input("Nº: "))
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print("Pares: ",pares)
print("Impares: ",impares)