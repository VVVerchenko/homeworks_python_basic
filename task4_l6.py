import random

class Car:
    def __init__(self, speed, color, name, police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        if self.is_police == True:
            police_text = "полицейский "
        else: police_text = ""
        print(f"{police_text}{self.color} {self.name} начал движение")

    def stop(self):
        print(f"{self.color} {self.name} остановился")

    def turn(self):
        direction = random.choice(["налево", "направо"])
        print(f"{self.color} {self.name} повернул {direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")

class TownCar(Car):
    def inf_auto(self):
        print(f"{self.color} {self.name} - это городской автомобиль")
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")
            print("Скорость превышена, допустимая скорость для городского транспорта - не более 60 км/ч")
        else:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")

class SportCar(Car):
    def inf_auto(self):
        print(f"{self.color} {self.name} - это спортивный автомобиль")

class WorkCar(Car):
    def inf_auto(self):
        print(f"{self.color} {self.name} - это служебный автомобиль")
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")
            print("Скорость превышена, допустимая скорость для служебного транспорта - не более 40 км/ч")
        else:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")

class PoliceCar(Car):
    def inf_auto(self):
        print(f"{self.color} {self.name} - это полицейский автомобиль")

car1 = TownCar(62, "белый", "Renault", True)
car2 = WorkCar(34, "бежевый", "Урал", False)
car3 = SportCar(200, "чёрный", "Lamborghini", False)

car1.inf_auto()
car1.show_speed()
car2.inf_auto()
car2.show_speed()
car3.inf_auto()
car3.show_speed()