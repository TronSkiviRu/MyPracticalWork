class Worker:

    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def GetSalary(self):
        print(f"Работник, {self.__surname} {self.__name}")
        print(f"Заработал: {self.__rate * self.__days}")

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days


worker1 = Worker("Игорь", "Скуталь", 2500, 30)
worker1.GetSalary()
print(worker1.get_rate())
print(worker1.get_days())

