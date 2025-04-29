class Student:
    def __init__(self, surname, birthday, gr_number, grade):
        self.surname = surname
        self.birthday = birthday
        self.gr_number = gr_number
        self.grade = grade

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday

    def change_gr_number(self, new_gr_number):
        self.gr_number = new_gr_number

    def change_grade(self, new_grade):
        if len(new_grade) == 5:
            self.grade = new_grade

    def info(self):
        print(f"Фамилия: {self.surname}; "
              f"Рожден: {self.birthday}; "
              f"Номер группы: {self.gr_number}; "
              f"Успеваемость: {self.grade}")


student1 = Student("Самойлов", "01.01.2001",
                   "602", [1, 2, 3, 4, 5])
student1.info()
student1.change_surname("Самолетов")
student1.change_birthday("02.02.2007")
student1.change_gr_number("632")
student1.change_grade([5, 5, 5, 5, 5])
student1.info()

student1.change_grade([99999999999])
student1.info()