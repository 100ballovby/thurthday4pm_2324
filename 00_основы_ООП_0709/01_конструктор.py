class Human:
    def __init__(self, gen, a, hair, status):  # конструктор класса
        """конструктор указывает некоторые (или все) параметры
        при создании экземпляра, все эти параметры нужны для
        конструирования объекта (у человека есть изначальный набор
        данных, которые ему нужны для дефолтного существования"""
        self.gender = gen  # "собственный" параметр gender берет значение из параметра gen
        self.age = a
        self.hair_color = hair
        self.programmer = status

    def __repr__(self):  # позволяет выводить нужную информацию об экземпляре в момент его вызова
        return f'Age: {self.age}, gender: {self.gender}'


oleg = Human('Male', 15, 'black', True)  # создание экземпляра класса Human
maxim = Human('Male', 14, 'white', False)  # другой экземпляр, который существует ОТДЕЛЬНО от Олега

maxim.age = 20
print(maxim)

