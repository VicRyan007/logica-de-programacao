idades = []
alturas = []
media = 0
anoes = 0
for i in range(4):
    idades.append(int(input("Idade: ")))
    alturas.append(float(input("Altura: ")))
    media+=alturas[i]
media =  media/4
for i in range(4):
    if idades[i]>13:
        if alturas[i]<media:
            anoes+=1
print("Quant. de alunos com altura abaixo da media: %d" %anoes)