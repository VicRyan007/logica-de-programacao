valor = int(input("Digite o valor: "))

quantC =0
quantD =0
quantU = 0

if valor<1000:
    if valor>=100:
        quantC = int(valor/100)
        quantD = int(valor/10)
        quantU = 0
print(quantC , " centenas")
print(quantD , " dezenas")
print(quantU , " unidades")