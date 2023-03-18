palavra = input("Digite uma palavra: ")
#tamanho = len(palavra)
#novaPalavra = " "
#for i in range(tamanho):
    #novaPalavra += palavra[i]
    #print(novaPalavra) 

for i in range(len(palavra)+1):
    print(palavra[:i])