filmes = {}
for i in range(5):
    nome_filme = input("Nome do filme: ")
    vilao = input("Vilão: ")
    ano_lancamento = input("Ano de lançamento: ")
    filmes[nome_filme] = [vilao,ano_lancamento]

while True :
    resp = input("Deseja pesquisar outro filme? (s/n) ")
    if resp == 'n':
        break
    if resp == 's':
        nome = input("Digite o nome do filme: ")
        for nome in filmes:
            vilao =list(filmes[nome].keys())[0]
            ano = filmes[nome][vilao] 
            if nome in filmes:
                print("Vilão: ",vilao)
                print("Ano ",ano)
            else:
                print("Não existe na lista\n")
        