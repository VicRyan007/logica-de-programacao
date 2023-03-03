ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
ladoC = float(input("Digite o valor do lado C: "))

if ladoA > ladoB-ladoC and ladoA < ladoB+ladoC or ladoB > ladoA-ladoC and ladoB < ladoA+ladoC or ladoC > ladoA-ladoB and ladoC < ladoA+ladoB:
    print("É um triângulo")
    if ladoA == ladoB and (ladoA and ladoB) != ladoC:
        print("do tipo isóceles")
    if ladoA == ladoB == ladoC:
        print("do tipo equilátero")
    if ladoA != ladoB != ladoC:
        print("do tipo escaleno")
else:
    print("Não é um triângulo")