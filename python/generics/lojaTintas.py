tamanhoAreaSerPintada = float(input("Tamanho da área a ser pintada: "))
litroTinta = 18
valorTinta = 80
litrosUsados = tamanhoAreaSerPintada/3
quantLatas = litrosUsados/litroTinta
valorTotal = quantLatas*valorTinta

if quantLatas % 54 == 0 :
    print("Quantidade de latas: %f" %quantLatas)
elif quantLatas % 54 != 0:
    print("Quantidade de latas: %f" %(quantLatas+1))

# 1l --- 3m
#18 ---- x
