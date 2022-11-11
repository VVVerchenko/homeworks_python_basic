class Worker:
    # атрибуты объкта
    def __init__(self, name, soname, position, income):
        self.n = name
        self.s = soname
        self.p = position
        self.__income = income

        self.wage = income["wage"]
        self.bonus = income["bonus"]

class Position(Worker):
    # метод получения полного имени
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.n} {self.s}")

    # метод получения информации о доходе
    def get_total_income(self):
        print(f"Доход сотрудника: {self.n} {self.s} составляет {self.wage + self.bonus}р")

worker1 = Position("Василий", "Иванов", "инженер", {"wage": 40000, "bonus": 20000})

worker1.get_full_name()
worker1.get_total_income()



