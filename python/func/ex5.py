def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

n = int(input("Digite um número inteiro: "))
digit_count = count_digits(n)
print("O número", n, "tem", digit_count, "dígitos.")
