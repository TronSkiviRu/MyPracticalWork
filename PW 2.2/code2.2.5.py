class MyClass:
    def __init__(self, property1=None, property2=None):
        self.property1 = property1
        self.property2 = property2
        print(f"Свойства назначены: {property1} и {property2}")

    def info(self):
        print(f"Свойства: {self.property1} {self.property2}")
        
    def __del__(self):
        print("Свойства удалены")


object1 = MyClass()
del object1
# object1.info() - будет ошибка
object1 = MyClass(777, True)

