num1 = int(input("Введите 1-е число: "))
num2 = int(input("Введите 2-е число: "))
num3 = int(input("Введите 3-е число: "))

def sum_of_largest_numbers(n1, n2, n3):
    numbers = [n1, n2, n3]
    min_num = min(numbers)
    numbers.remove(min_num)
    sum_max = numbers[0] + numbers[1]
    return sum_max

print(sum_of_largest_numbers(num1, num2, num3))