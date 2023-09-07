class Human:
    gender = ''
    age = 0
    hair_color = ''
    programmer = False

oleg = Human()  # создание экземпляра класса Human
maxim = Human()  # другой экземпляр, который существует ОТДЕЛЬНО от Олега
oleg.programmer = True  # название параметра класса programmer (установить для олега programmer в True)

print(maxim.programmer)
print(oleg.programmer)
