num = float(input("Digite um número: "))

if num%3==0:
    print("O número %d é divísivel por 3"%num)

if num%4==0:
    print("O número %d é divísivel por 4"%num)

if num%3==0 and num%4==0:
    print("O número %d é divísivel por 3 e 4"%num)