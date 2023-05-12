#  7. Utilizando funções, leia um número inteiro e retorne o seu equivalente em
# numeração romana.

def roma(num):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    return result

num = int(input("Digite um número inteiro: "))
roman_numeral = roma(num)
print("O número", num, "em numeração romana é", roman_numeral)
