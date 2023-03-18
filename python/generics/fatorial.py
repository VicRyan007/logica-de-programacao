num = int(input("Digite um número: "))
print(num,"! = ", end= "")
while num!=0:
    fatorial = num * (num - 1) 
    fatorial*=num
    print(num , end=' ')
    num-=1
