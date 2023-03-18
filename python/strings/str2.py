nome = input("Digite seu nome: ")
nomeContrario = " "
tamanho = len(nome)-1

while tamanho !=-1:
    nomeContrario += nome[tamanho]
    tamanho-=1

print(nomeContrario.upper())


