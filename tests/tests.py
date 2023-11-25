class MyClass:
    c = 0  # переменная класса
    g = 0

    def __init__(self):
        self.i = 0
        self.i += 1
        MyClass.set_tick(1)
        MyClass.g += 1
        print(self.i, MyClass.c, MyClass.g)

    # Метод класса
    @classmethod
    def set_tick(cls, nv):
        cls.c += nv

# Создание объектов класса
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj1.set_tick(10)
obj4 = MyClass()
obj5 = MyClass()
obj6 = MyClass()
obj6.set_tick(10)
obj7 = MyClass()
