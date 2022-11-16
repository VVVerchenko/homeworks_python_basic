class ZeroDiv(Exception):
    def __init__(self, numb):
        self.numb = numb

num1 = int(input('Введите делимое: '))
num2 = int(input('Введите делитель: '))

try:
    if num2 == 0:
        raise ZeroDiv('На ноль делить нельзя!')
except (ValueError, ZeroDiv) as err:
    print(err)
else:
    print(num1 / num2)
finally:
    print('Конец')