import time

class TrafficLight:

    def __init__(self):
        self.__color = "цвет"

    # метод работы светофора
    def running(self):
        while True:
            self.__color = "красный"
            print(self.__color)
            time.sleep(7)
            self.__color = "желтый"
            print(self.__color)
            time.sleep(2)
            self.__color = "зелёный"
            print(self.__color)
            time.sleep(5)
            self.__color = "желтый"
            print(self.__color)
            time.sleep(2)

tl1 = TrafficLight()
tl1.running()