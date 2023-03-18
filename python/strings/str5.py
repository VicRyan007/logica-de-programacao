palavra = input("Digite uma palavra: ")
palavra = palavra.replace(" ","")
palindronoOuNao = palavra[::-1]

if (palavra == palindronoOuNao):
    print("É palíndromo")
else:
    print("Não é palíndromo")

print(palindronoOuNao)