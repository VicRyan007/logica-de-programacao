resp = False
salariosTotais = 0
totalFilhos = 0
quantidadeSalarios = 0
salMaior = 0
pais = 0


while resp == False:
    sal = float(input("Digite o salario: R$ "))
    if sal<0:
        totalFilhos/=pais
        break
    filhos = float(input("Digite a quantidade de filhos: "))
    quantidadeSalarios+=1
    if filhos>0:
        pais+=1
        totalFilhos+=filhos
    if sal>salMaior:
        salMaior =  sal
    else:
        sal = salMaior
    salariosTotais+=sal     
salariosTotais/=quantidadeSalarios
    

print("Média de salário: R$ %.2f" %salariosTotais)
print("Média do número de filhos por casa: %d filhos" %totalFilhos)
print("Maior salário: R$ %.2f" %salMaior)
# print("Percentual de pessoa com salário menor que R$ 150,00: ", )
    