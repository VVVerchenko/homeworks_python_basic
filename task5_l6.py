class Stationely:
    # атрибуты класса
    title = "название"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationely):
    def draw(self):
        print("Рисуем ручкой")

class Pencil(Stationely):
    def draw(self):
        print("Рисуем карандашом")

class Handle(Stationely):
    def draw(self):
        print("Рисуем маркером")

pen1 = Pen()
pencil1 = Pencil()
handle1 = Handle()

pen1.draw()
pencil1.draw()
handle1.draw()