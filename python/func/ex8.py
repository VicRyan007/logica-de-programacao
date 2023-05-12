# Estrutura do dicionário:
# dic = {'chave': 1}

def incluirNovoNome(dic) :
    nome = input("Digite o nome que deseja digitar: ")
    quant_phone = int(input("Quantidade de telefones: "))
    for i in range(quant_phone):
        dic[nome] = ' '

def incluirTelefone(dic):
    nome = input("Nome: ")
    if 'nome' in dic:
        phone = input("Telefone: ")
        dic[nome] = phone
    else:
        resp = input("Deseja incluir o nome na lista ?")
        if resp == "Sim" or resp == "sim":
            phone = input("Telefone: ")
            dic[nome] = phone
        elif resp == "Não" or resp == "não":
            print("ok")

def excluirTelefone(dic):
    nome = input("Nome: ")
    if 'nome' in dic:
        if len(dic[nome]) > 1:
            for i in range(1):
                dic.pop(nome)
    else:
        dic.pop(nome)

def excluirNome(dic):
    nome = input("Nome: ")
    if len(dic[nome])>1:
        for i in range(len(dic[nome])):
            dic.pop(nome)
    else:
        dic.pop(nome)

def consultarTelefone(dic):
    nome = input("Nome: ")
    if nome in dic:
        for nome in dic:
            print(dic[nome])