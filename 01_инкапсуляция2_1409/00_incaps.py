class Laptop:
    """private от protected отличается количеством _, в private их 2, в protected 1"""
    _cycle_count = 0  # protected-поле (оно защищено, но доступ к нему получить можно)
    __serial_number = '1x2afkury324084'  # private-поле (доступ вообще запрещен, но это не точно)
    def __init__(self, n, num):
        self.name = n
        self.number = num

    def turn_on(self):  # public-метод (полный доступ)
        print('Welcome!')

    def charge(self):
        self._cycle_count += 1
        print(f'Battery charged {self._cycle_count} times.')

    def __lt__(self, other):  # public-метод
        """Расширенное сравнение. Определяет правила для сравнения двух
        объектов пользовательского класса. Эти методы не попадают под
        определение инкапсуляции"""
        return self.number < other.number


l1 = Laptop('My notebook', 20)
l2 = Laptop('Another_notebook', 30)

# сравнение всеми доступными операторами возможно
print(l1 < l2)
print(l1 > l2)
print(l1 == l2)

l1.turn_on()
l1._cycle_count += 5  # доступ к protected полям получить можно, если вы знаете, как они называются
l1.charge()
# для обхода инкапсуляции используется шаблон: экземпляр._Класс__приватное_поле
l1._Laptop__serial_number = 'drugoy_seriinik'
print(f'Serial number: {l1._Laptop__serial_number}')



