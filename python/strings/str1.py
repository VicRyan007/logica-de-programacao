str1 = input(" String 1: ")
str2 = input(" String 2: ")
print("Conteúdo da String 1: "+str1+" -- Tamanho:",len(str1)) # type: ignore
print("Conteúdo da String 2: "+str2+" -- Tamanho:",len(str2))
if(len(str1) == len(str2)):
        print("Possuem o mesmo tamanho")
else:
        print("Não possuem o mesmo tamanho")

if(str1 == str2):
        print("Possuem o mesmo conteúdo")
else:
        print("Não possuem o mesmo conteúdo")