num1 = int(input("Введите 1-е число: "))
num2 = int(input("Введите 2-е число: "))

def division(n1, n2):
    try:
        result = n1 / n2
        print(result)
    except ZeroDivisionError:
        print("Делить на ноль нельзя!!!")

division(num1,num2)