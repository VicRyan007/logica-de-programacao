data = input("Data: ")
data = data.split("/")
meses = {
    1:"janeiro",
    2:"fevereiro",
    3:"março",
    4:"abril",
    5:"maio",
    6:"junho",
    7:"julho",
    8:"agosto",
    9:"setembro",
    10:"outubro",
    11:"novembro",
    12:"dezembro",
}

# for i in range(len(meses)-1):
#     if data[1] == meses[i]:
#         print(f"Você nasceu em {data[0]} de {meses[i]} {data[2]}")