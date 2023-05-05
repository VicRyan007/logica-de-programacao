lista = [1,4,5,3,7,-4,3,102,394,98,-12,11,-40,-100]
menor = 0
maior = 0
for n in lista:
    if n>maior:
        maior = n
    if maior>n:
        menor = n

print("Menor: ", menor)
print("Maior: ", maior)