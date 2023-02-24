idade1 = 10
idade2 = 12
idade3 = 15
idade4 = 17

media = (idade1+idade2+idade3+idade4)/4
print("Média: ", media)
media2 = (idade1+idade2+idade3+idade4+16)/5

variacaoPerc = (media2*100)/media - 100

print("Variação percentual ao adicionar uma pessoa de 16 anos: %.2f" % (variacaoPerc), "%")


# media -- 100%
#media2 -- x