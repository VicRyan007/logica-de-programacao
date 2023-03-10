num1 = int(input("Nº1 : "))
num2 = int(input("Nº2 : "))
numsPares = 0

for i in range(num1,num2):
    if i%2==0:
        numsPares+=1
print(numsPares)