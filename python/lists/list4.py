idades = []
alturas = []
media = 0
anoes = 0
n = int(input("Digite a quantidade de alunos a serem cadastrados: "))
for i in range(n):
    idades.append(int(input("Idade: ")))
    alturas.append(float(input("Altura: ")))
    media+=alturas[i]
media =  media/n
for i in range(n):
    if idades[i]>13:
        if alturas[i]<media:
            anoes+=1
print("Quant. de alunos com altura abaixo da media: %d" %anoes)