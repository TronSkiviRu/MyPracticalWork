class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        print(f"Работник, {self.surname} {self.name}")
        print(f"Заработал: {self.rate * self.days}")


worker1 = Worker("Игорь", "Скуталь", 2500, 30)
worker1.get_salary()
