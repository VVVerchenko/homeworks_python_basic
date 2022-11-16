compl_num1 = complex(5, 3)
compl_num2 = complex(4, 8)

print("Расчёт через стандартные функции:")
print(f'{compl_num1} + {compl_num2} = {compl_num1 + compl_num2}')
print(f'{compl_num1} * {compl_num2} = {compl_num1 * compl_num2}')

class СomplexNumbers:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return СomplexNumbers(self.re + other.re, self.im + other.im)
    def __str__(self):
        return f"{self.re} + j{self.im}"

    def __mul__(self, other):
        return СomplexNumbers(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)
    def __str__(self):
        return f"{self.re} + j{self.im}"

compl_num1 = СomplexNumbers(5, 3)
compl_num2 = СomplexNumbers(4, 8)

print("\nРасчёт через переопределение:")
print(f'({compl_num1.re}+j{compl_num1.im}) + ({compl_num2.re}+j{compl_num2.im}) = {compl_num1 + compl_num2}')
print(f'({compl_num1.re}+j{compl_num1.im}) * ({compl_num2.re}+j{compl_num2.im}) = {compl_num1 * compl_num2}')
