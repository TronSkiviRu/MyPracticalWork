class WorkTwoNums:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def max_nums(self):
        if self.num1 > self.num2:
            answer = self.num1
        else:
            answer = self.num2
        print("Максимальное число", answer)

    def sum_nums(self):
        print("Сумма этих чисел: ", self.num1 + self.num2)

    def change_first_num(self, new_num):
        self.num1 = new_num

    def change_second_num(self, new_num):
        self.num2 = new_num

    def info(self):
        print(f"Число_1: {self.num1}; Число_2: {self.num2}")


work1 = WorkTwoNums(1, 2)
work1.info()
work1.max_nums()
work1.sum_nums()

work1.change_first_num(-3)
work1.change_second_num(3)
work1.info()
work1.max_nums()
work1.sum_nums()
