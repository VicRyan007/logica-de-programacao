valor = float(input("Digite o valor: "))
code = int(input("Digite o valor do código: "))

if code==1 :
    print("À vista em dinheiro ou cheque, recebe 10%"+" de desconto")
    print("Valor com desconto: R$ %.2f"%(valor-(valor*0.1)))
elif code==2 :
    print("À vista no cartão de crédito, recebe 15%"+" de desconto")
    print("Valor com desconto: R$ %.2f"%(valor-(valor*0.15)))
elif code==3 :
    print("Em duas vezes, preço normal de etiqueta sem juros")
    print("Valor s/desconto: R$ %.2f"%valor)
elif code==4 :
    print("Em três vezes, preço normal de etiqueta mais juros de 10%")
    print("Valor com juros: R$ %.2f"%(valor+(valor*0.1)))
elif code==5 :
    print("Em seis vezes, preço normal de etiqueta mais juros de 20%")
    print("Valor com juros: R$ %.2f"%(valor+(valor*0.2)))