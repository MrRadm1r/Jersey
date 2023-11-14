class Cat:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    cat1 = Cat('Tom')
    cat2 = Cat('Tom')
    print(cat1 == cat2)
