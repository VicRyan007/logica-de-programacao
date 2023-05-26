    # 4. Um problema típico em ciência da computação consiste em converter um número da sua
    # forma decimal para a forma binária. Crie uma função recursiva que execute essa conversão.

# Para se converter um número de decimal para binário, usa-se o resto
def dec_para_bin(n):
    if n == 0:
        return 0
    bin = ''
    resto = n%2
    bin = str(resto) + bin
    return bin + str(dec_para_bin(n//2)) 
    


print(dec_para_bin(10))
print(dec_para_bin(4))