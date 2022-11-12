class Cell:
    def __init__(self, amount):
        self.am = amount

    def __add__(self, other):
        return self.am + other.am

    def __sub__(self, other):
        if self.am - other.am > 0:
            return self.am - other.am
        else: return "Разность должна быть больше нуля"

    def __mul__(self, other):
        return self.am * other.am

    def __truediv__(self, other):
        return self.am // other.am

    def make_order(self, row_amount):
        self.ra = row_amount
        current_am = self.am
        current_list = []

        while current_am > 0:
            if current_am > self.ra:
                for i in range(self.ra):
                    current_list.append("*")
                    current_am -= 1
                current_list.append("\n")
            else:
                for i in range(current_am):
                    current_list.append("*")
                    current_am -= 1
        return ''.join(current_list)

a = Cell(12)
b = Cell(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a.make_order(5))