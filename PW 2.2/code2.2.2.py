class Train:
    def __init__(self, path, number_train, time_run):
        self.path = path
        self.number_train = number_train
        self.time_run = time_run

    def info(self):
        print(f"Пункт назначения: {self.path}; "
              f"Номер поезда: {self.number_train}; "
              f"Время выезда: {self.time_run}")


train1 = Train("Барселона", 666, "11.00")
train1.info()