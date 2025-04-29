class Train:
    train_array = {}

    def __init__(self, path, number_train, time_run):
        self.train_array[number_train] = (path, number_train, time_run)
        self.number_train = number_train

    @classmethod
    def find_train_info(cls, number):
        try:
            path, number_train, time_run = cls.train_array[number]
            print(f"Пункт назначения: {path}; "
                  f"Номер поезда: {number_train}; "
                  f"Время выезда: {time_run}")
        except KeyError:
            print("Неверный номер поезда")

    def __del__(self):
        del self.train_array[self.number_train]


train1 = Train("Барселона-Кипр", 666, "11.00")
train2 = Train("Барселона-Москва", 686, "11.00")
Train.find_train_info(666)
Train.find_train_info(6860)
train1.find_train_info(686)
del train2
print(train1.train_array)

