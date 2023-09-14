class Book:
    def __init__(self, title, author, year, is_available):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__is_available = is_available

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_year(self, year):
        self.__year = year

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_avail(self):
        return self.__is_available

    def switch_availability(self):
        """
        Переключает статус наличия книги
        :return: None
        """
        if self.__is_available:  # если книга сейчас доступна
            self.__is_available = False  # мы ее бронируем
        else:  # иначе
            self.__is_available = True  # делаем ее доступной


alice = Book('Alice in Wonderland', 'ekrjfgh', 1960, True)
print(alice.get_avail())
print('книгу выдали')
alice.switch_availability()
print(alice.get_avail())
print('книгу вернули')
alice.switch_availability()
print(alice.get_avail())

