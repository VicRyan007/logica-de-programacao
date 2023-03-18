# Usar replace() e find()
# A-T G-C

cadeia = input("Digite a cadeia: ")
cadeia = cadeia.upper()

for i in list(cadeia):
    if(i == 'A'):
       print( cadeia.replace('A','T'))
    elif(i == 'T'):
       print( cadeia.replace('T','A'))
    elif(i == 'G'):
       print( cadeia.replace('G','C'))
    elif(i == 'C'):
       print( cadeia.replace('C','G'))

    