class Road:
    # атрибуты класса
    mass_psn = 25
    thickness = 5

    # атрибуты объекта
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calculation(self):
        mass = self.__length * self.__width * Road.mass_psn * Road.thickness / 1000
        print(f"Общая масса асфальта составляет: {mass} тонн")

road1 = Road(20, 5000)
road1.mass_calculation()
