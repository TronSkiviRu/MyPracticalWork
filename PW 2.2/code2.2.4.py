class Counter:
    def __init__(self, used_value=0):
        self.used_value = used_value

    def plus_one(self):
        self.used_value += 1

    def minus_one(self):
        self.used_value -= 1

    def info(self):
        print(f"Число в счетчике: {self.used_value}")


counter1 = Counter()
counter1.info()
[counter1.plus_one() for _ in range(10)]
counter1.info()
print("-"*20)
counter2 = Counter(99)
counter2.info()
counter2.minus_one()
counter2.plus_one()
counter2.plus_one()
counter2.info()

