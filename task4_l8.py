class Warehouse:
    """Базовый класс - склад оргтехники"""
    company_name = "DNS"
    warehouse_address = "Россия, г. Челябинск, ул. Радонежская, д. 15"

class OfficeEquipment(Warehouse):
    """Класс - оргтехника"""
    product_class_name = "Оргтехника"

class Printer(OfficeEquipment):
    """Класс - принтер"""
    product_type_name = "Принтер"
    product_function = "Функция печати документации"

class Scanner(OfficeEquipment):
    """Класс - сканер"""
    product_type_name = "Сканер"
    product_function = "Функция сканирования документации"

class Xerox(OfficeEquipment):
    """Класс - ксерокс"""
    product_type_name = "Копировальный аппарат"
    product_function = "Функция копирования документации"

