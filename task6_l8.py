class DigitValidation(Exception):
    def __init__(self,num):
        self.n = num

class RangeValidation(Exception):
    def __init__(self,num):
        self.n = num

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
    # Запрос категории товара
    product_type_input = input("Введите категорию товара:\n"
                                   "1 - Принтеры\n"
                                   "2 - Сканеры\n"
                                   "3 - Ксероксы\n")
    try:
        if (product_type_input.isdigit() == False) or (int(product_type_input) < 1 or int(product_type_input) > 3):
            raise RangeValidation('\nВведите корректный номер категории\n')
    except (RangeValidation) as err:
        print(err)
    else:

        # Запрос типа операции
        operation_type_input = input("Введите тип операции:\n"
                                     "1 - Получение\n"
                                     "2 - Отправка\n"
                                     "3 - Информация о товаре\n")

        try:
            if (operation_type_input.isdigit() == False) or (int(operation_type_input) < 1 or int(operation_type_input) > 3):
                raise RangeValidation('\nВведите корректный номер операции\n')
        except (RangeValidation) as err:
            print(err)
        else:

            # Получение и отправка принтеров
            if int(product_type_input) == 1:
                if int(operation_type_input) == 1:
                    res_am = input("Введите количество полученных принтеров: ")
                    try:
                        if res_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        res_printers = Printer(int(res_am))
                        res_printers.receiving()
                        print(f"\nТекущее количество товаров:\n{res_printers.current_amount_dict}\n")
                    finally: pass

                elif int(operation_type_input) == 2:
                    sent_am = input("Введите количество отправленных принтеров: ")
                    try:
                        if sent_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        if int(sent_am) > Warehouse.current_amount_dict["Принтер"]:
                            print("\nКоличество товара на складе не достаточно\n")
                        else:
                            sent_printers = Printer(int(sent_am))
                            sent_printers.sending()
                            print(f"\nТекущее количество товаров:\n{sent_printers.current_amount_dict}\n")

                elif int(operation_type_input) == 3:
                    printer1 = Printer
                    print(f"\nОборудование принадлежит: {printer1.company_name}\n"
                          f"Находится на складе по адресу: {printer1.warehouse_address}\n"
                          f"Тип оборудования: {printer1.product_type_name}\n"
                          f"Назначение: {printer1.product_function}\n")

            # Получение и отправка сканеров
            elif int(product_type_input) == 2:
                if int(operation_type_input) == 1:
                    res_am = input("Введите количество полученных сканеров: ")
                    try:
                        if res_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        res_scanners = Scanner(res_am)
                        res_scanners.receiving()
                        print(f"\nТекущее количество товаров:\n{res_scanners.current_amount_dict}\n")

                elif int(operation_type_input) == 2:
                    sent_am = input("Введите количество отправленных сканеров: ")
                    try:
                        if sent_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        if int(sent_am) > Warehouse.current_amount_dict["Сканер"]:
                            print("\nКоличество товара на складе не достаточно\n")
                        else:
                            sent_scanners = Scanner(sent_am)
                            sent_scanners.sending()
                            print(f"\nТекущее количество товаров:\n{sent_scanners.current_amount_dict}\n")

                elif int(operation_type_input) == 3:
                    scanner1 = Scanner
                    print(f"\nОборудование принадлежит: {scanner1.company_name}\n"
                          f"Находится на складе по адресу: {scanner1.warehouse_address}\n"
                          f"Тип оборудования: {scanner1.product_type_name}\n"
                          f"Назначение: {scanner1.product_function}\n")

            # Получение и отправка ксероксов
            elif int(product_type_input) == 3:
                if int(operation_type_input) == 1:
                    res_am = input("Введите количество полученных ксероксов: ")
                    try:
                        if res_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        res_xerox = Xerox(res_am)
                        res_xerox.receiving()
                        print(f"\nТекущее количество товаров:\n{res_xerox.current_amount_dict}\n")

                elif int(operation_type_input) == 2:
                    sent_am = input("Введите количество отправленных ксероксов: ")
                    try:
                        if sent_am.isdigit() == False:
                            raise DigitValidation('\nНеобходимо ввести число\n')
                    except (ValueError, DigitValidation) as err:
                        print(err)
                    else:
                        if int(sent_am) > Warehouse.current_amount_dict["Ксерокс"]:
                            print("\nКоличество товара на складе не достаточно\n")
                        else:
                            sent_xerox = Xerox(sent_am)
                            sent_xerox.sending()
                            print(f"\nТекущее количество товаров:\n{sent_xerox.current_amount_dict}\n")

                elif int(operation_type_input) == 3:
                    xerox1 = Xerox
                    print(f"\nОборудование принадлежит: {xerox1.company_name}\n"
                          f"Находится на складе по адресу: {xerox1.warehouse_address}\n"
                          f"Тип оборудования: {xerox1.product_type_name}\n"
                          f"Назначение: {xerox1.product_function}\n")