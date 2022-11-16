class Warehouse:
    """Базовый класс - склад оргтехники"""
    company_name = "DNS"
    warehouse_address = "Россия, г. Челябинск, ул. Радонежская, д. 15"

    current_amount_dict = {"Принтер": 0, "Сканер": 0, "Ксерокс": 0}
    current_amount = 0

class OfficeEquipment(Warehouse):
    """Класс - оргтехника"""
    product_class_name = "Оргтехника"

class Printer(OfficeEquipment):
    """Класс - принтер"""
    product_type_name = "Принтер"
    product_function = "Функция печати документации"

    def __init__(self, amount):
        self.amount = amount

    def receiving(self):
        Warehouse.current_amount_dict["Принтер"] += self.amount

    def sending(self):
        Warehouse.current_amount_dict["Принтер"] -= self.amount

class Scanner(OfficeEquipment):
    """Класс - сканер"""
    product_type_name = "Сканер"
    product_function = "Функция сканирования документации"

    def __init__(self, amount):
        self.amount = amount

    def receiving(self):
        Warehouse.current_amount_dict["Сканер"] += self.amount

    def sending(self):
        Warehouse.current_amount_dict["Сканер"] -= self.amount

class Xerox(OfficeEquipment):
    """Класс - ксерокс"""
    product_type_name = "Копировальный аппарат"
    product_function = "Функция копирования документации"

    def __init__(self, amount):
        self.amount = amount

    def receiving(self):
        Warehouse.current_amount_dict["Ксерокс"] += self.amount

    def sending(self):
        Warehouse.current_amount_dict["Ксерокс"] -= self.amount

while True:
    product_type_input = int(input("Введите категорию товара:\n"
                                   "1 - Принтеры\n"
                                   "2 - Сканеры\n"
                                   "3 - Ксероксы\n"))
    if product_type_input == 1:
        operation_type_input = int(input("Введите тип операции:\n"
                                         "1 - Получение\n"
                                         "2 - Отправка\n"))
        if operation_type_input == 1:
            res_am = int(input("Введите количество полученных принтеров: "))
            res_printers = Printer(res_am)
            res_printers.receiving()
            print(f"\nТекущее количество товаров:\n{res_printers.current_amount_dict}\n")

        elif operation_type_input == 2:
            sent_am = int(input("Введите количество отправленных принтеров: "))
            sent_printers = Printer(sent_am)
            sent_printers.sending()
            print(f"\nТекущее количество товаров:\n{sent_printers.current_amount_dict}\n")

    elif product_type_input == 2:
        operation_type_input = int(input("Введите тип операции:\n"
                                         "1 - Получение\n"
                                         "2 - Отправка\n"))

        if operation_type_input == 1:
            res_am = int(input("Введите количество полученных сканеров: "))
            res_scanners = Scanner(res_am)
            res_scanners.receiving()
            print(f"\nТекущее количество товаров:\n{res_scanners.current_amount_dict}\n")

        elif operation_type_input == 2:
            sent_am = int(input("Введите количество отправленных сканеров: "))
            sent_scanners = Scanner(sent_am)
            sent_scanners.sending()
            print(f"\nТекущее количество товаров:\n{sent_scanners.current_amount_dict}\n")

    elif product_type_input == 3:
        operation_type_input = int(input("Введите тип операции:\n"
                                         "1 - Получение\n"
                                         "2 - Отправка\n"))

        if operation_type_input == 1:
            res_am = int(input("Введите количество полученных ксероксов: "))
            res_xerox = Xerox(res_am)
            res_xerox.receiving()
            print(f"\nТекущее количество товаров:\n{res_xerox.current_amount_dict}\n")

        elif operation_type_input == 2:
            sent_am = int(input("Введите количество отправленных ксероксов: "))
            sent_xerox = Xerox(sent_am)
            sent_xerox.sending()
            print(f"\nТекущее количество товаров:\n{sent_xerox.current_amount_dict}\n")