meses = [
    "1 -janeiro",
    "2 - fevereiro",
    "3 - março",
    "4 - abril",
    "5 - maio",
    "6 - junho",
    "7 - julho",
    "8 - agosto",
    "9 - setembro",
    "10 - outubro",
    "11 - novembro",
    "12 - dezembro"
]

temperatura = []
media = 0 
for i in range(len(meses)-1):
    n = float(input("Tempº : "))
    media += n
    temperatura.append(n)
media/=12

for i in range(len(temperatura)-1):
    if temperatura[i]>media:
        print(f"{meses[i]}: {temperatura[i]}º")