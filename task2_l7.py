from abc import ABC, abstractmethod

class Wear(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Coat(Wear):
    def __init__(self, v):
        self.__v = v

    @property
    def calculate(self):
        return self.__v

    @calculate.setter
    def calculate(self, v):
        if v < 44:
            self.__v = 44
        elif v > 68:
            self.__v = 68
        else:
            self.__v = v

    def __str__(self):
        return f"Расход ткани на пальто для размера {self.__v} составит: {str(round(self.__v / 6.5 + 0.5, 2))} м2"

class Suit(Wear):
    def __init__(self, h):
        self.__h = h

    @property
    def calculate(self):
        return self.__h

    @calculate.setter
    def calculate(self, h):
        if h < 1.7:
            self.__h = 1.7
        elif h > 2:
            self.__h = 2
        else:
            self.__h = h

    def __str__(self):
        return f"Расход ткани на костюм для роста {self.__h} м составит: {str(round(2 * self.__h + 0.3, 2))} м2"


coat1 = Coat(46)
coat1.calculate = 46
print(coat1)

suit1 = Suit(1.8)
suit1.calculate = 1.8
print(suit1)