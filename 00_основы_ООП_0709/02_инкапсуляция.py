class Human:
    def __init__(self, gen, a, hair, status):  # конструктор класса
        """конструктор указывает некоторые (или все) параметры
        при создании экземпляра, все эти параметры нужны для
        конструирования объекта (у человека есть изначальный набор
        данных, которые ему нужны для дефолтного существования"""
        self.gender = gen  # "собственный" параметр gender берет значение из параметра gen
        self.__age = a  # условная инкапсуляция (сокрытие данных)
        self.hair_color = hair
        self.programmer = status

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print('Incorrect')

    def birthday(self):
        self.__age += 1

    def get_age(self):
        print(self.__age)

    def __repr__(self):  # позволяет выводить нужную информацию об экземпляре в момент его вызова
        return f'Age: {self.__age}, gender: {self.gender}'


oleg = Human('Male', 15, 'black', True)  # создание экземпляра класса Human
maxim = Human('Male', 14, 'white', False)  # другой экземпляр, который существует ОТДЕЛЬНО от Олега

print(maxim.get_age())
maxim.birthday()
print(maxim)

