valor = int(input("Digite o valor: "))

quantC =0
quantD =0
quantU = 0

if valor<1000:
        quantC = int(valor/100)
        quantD = int((valor-(quantC*100))/10)
        quantU = int(valor-(quantC*100)-(quantD*100)/10)
print(quantC , " centenas")
print(quantD , " dezenas")
print(quantU , " unidades")