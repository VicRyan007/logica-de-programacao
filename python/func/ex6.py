def pot(a,b):
    result = 1
    if type(a) == int and type(b)== int:
        for i in range(b):
            result *=a
    return result


print(pot(2,5))
print(pot(5,2))
print(pot(10,2))