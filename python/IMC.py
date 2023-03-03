massa = float(input("Digite sua massa (peso): "))
altura = float(input("Digite sua altura: "))

imc = massa/(altura*altura)

print("IMC: %.2f" %imc)
if imc<20:
    print("Seu IMC está abaixo do normal")
elif 20<imc<25:
    print("Seu IMC está normal")
elif 25<imc<30:
    print("Você está com sobrepeso")
elif 30<imc<35:
    print("Você está com obesidade leve")
elif 35<imc<40:
    print("Você está com obesidade moderada")
elif imc>=40:
    print("Você está com obesidade mórbida")