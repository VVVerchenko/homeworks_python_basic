x = int(input("Введите положительное основание степени: "))
y = int(input("Введите отрицательный показатель степени: "))

def my_func1(x, y):
    res = x**y
    return res

def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res = res * (1 / x)
    return res

print(my_func1(x,y))
print(my_func2(x,y))