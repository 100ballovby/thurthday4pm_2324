class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__grad_list = []

    def add_grade(self, *grade):
        for i in grade:
            self.__grad_list.append(i)

    def get_average_grade(self):
        return sum(self.__grad_list) / len(self.__grad_list)


alex = Student('Alex', 21)
alex.add_grade(5, 5, 2, 3)
alex.add_grade(5)

print(alex.get_average_grade())

