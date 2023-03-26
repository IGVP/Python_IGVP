class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __str__(self):
        return f'Объект с параметрами  ({self.param1}, {self.param2})'


obj = MyClass(2, 2)
print(MyClass.__str__(obj))
