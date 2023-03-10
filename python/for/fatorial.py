num = int(input("Digite um número: "))
print(num,"! = ", end= "")
for i in range(num):
    fatorial = num * (num - 1) 
    fatorial*=num
    print(num , end=' ')
    num-=1