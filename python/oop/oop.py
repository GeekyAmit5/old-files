class oop:
    def __init__(self):
        print("oop")

    def hi(self):
        print("hi")


class oo(oop):
    def __init__(self):
        print("oo")
        super().__init__()
        super().hi()
        oop.hi(self)


o2 = oo()

print(oo.__mro__)
