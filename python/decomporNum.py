valor = int(input("Digite o valor: "))

quantC =0
quantD =0
quantU = 0

if valor<1000:
        quantC = int(valor/100)
        quantD = int((valor-(quantC*100))/10)
        quantU = int(valor-(quantC*100)-(quantD*100)/10)
if quantC>0:print(quantC , " centenas")
if quantD>0:print(quantD , " dezenas")
if quantU>0:print(quantU , " unidades")