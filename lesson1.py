"""НАСЛЕДОВАНИЕ"""


class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def info(self):
        print(f'Птица {self.name}, цвет: {self.color}, звук: {self.voice}')

    def fly(self):
        print(f'{self.name} летает')

    def sing(self):
        print(f'{self.name} поёт - {self.voice}')

    def eat(self):
        print(f'{self.name} ест')


class Golub(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f'{self.name} ходит')

    def sing(self):
        print(print(f'{self.name} поёт - lalala'))


bird1 = Golub('Гоша', 'Кря-кря', 'Серый', 'Кукуруза')
bird2 = Bird('Masha', 'Chirik-chirik', 'Black')

#bird1.info()
#bird1.sing()

#bird2.info()
#bird2.sing()

"""ИНКАПСУЛЯЦИЯ"""


class Test():
    def __init__(self):
        self.__a = 'private'
        self._b = 'protected'
        self.c = 'public'

    def get_private(self):
        return self.__a

    def set_private(self, value):
        self.__a = value

    def public_method(self):
        print('public method')

    def _protected_method(self):
        print('protected method')

    def __private_method(self):
        print('private method')

    def test_private(self):
        self.__private_method()

test = Test()
print(test.c)
print(test._b)
print(test.get_private())

test.set_private('new value')
print(test.get_private())

test.public_method()
test._protected_method()
test.test_private()