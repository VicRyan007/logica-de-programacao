lista = ['caso','casa','algo','além','caso','casa']
resultado = {}
for l in range (len(lista)):
    resultado[lista[l]] = lista.count(lista[l])

print(resultado)