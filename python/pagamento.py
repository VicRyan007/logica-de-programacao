hora = float(input("Digite as horas trabalhadas: "))
valorHora = float(input("Digite o valor da horas: "))
salarioBruto = hora*valorHora

desconto5 = 0.05
desconto10 = 0.1
desconto20 = 0.2

if salarioBruto<=900:
    print("Salário líquido: R$ %.2f" %salarioBruto)
elif salarioBruto<=1500:
    print("Salário líquido: R$ %.2f" %(salarioBruto-(salarioBruto*desconto5)))
elif salarioBruto<=2500:
    print("Salário líquido: R$ %.2f" %(salarioBruto-(salarioBruto*desconto10)))
elif salarioBruto>2000:
    print("Salário líquido: R$ %.2f" %(salarioBruto-(salarioBruto*desconto20)))
