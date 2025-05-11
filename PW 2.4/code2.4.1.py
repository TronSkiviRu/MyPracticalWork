import sqlite3

BD_NAME = "university.bd"


class Student:

    def __init__(self, name: str, surname: str, patronymic: str, group: str, grade: list, id =None):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.grade = grade
        self.id = id


def remake_student_bd(action, value, sid):
    con = sqlite3.connect(BD_NAME)
    cursor = con.cursor()

    match action:
        case "name":
            name1, name2, name3 = value.split()
            cursor.execute("UPDATE students SET first_name =? WHERE id=(?)", (name1, sid))
            cursor.execute("UPDATE students SET last_name =? WHERE id=(?)", (name2, sid))
            cursor.execute("UPDATE students SET patronymic =? WHERE id=(?)", (name3, sid))
        case "group":
            cursor.execute("UPDATE students SET group_name =? WHERE id=(?)", (value, sid ))
        case "grade":
            grade1, grade2, grade3, grade4 = value.split()
            cursor.execute("UPDATE students SET grade1 =? WHERE id=(?)", (grade1, sid))
            cursor.execute("UPDATE students SET grade2 =? WHERE id=(?)", (grade2, sid))
            cursor.execute("UPDATE students SET grade3 =? WHERE id=(?)", (grade3, sid))
            cursor.execute("UPDATE students SET grade4 =? WHERE id=(?)", (grade4, sid))
    con.commit()
    con.close()

    if cursor.rowcount == 0:
        print("Запись с таким ID не найдена.")
    else:
        print("Обновление выполнено успешно.")

def add_student_bd(student):
    con = sqlite3.connect(BD_NAME)
    cursor = con.cursor()
    grade = student.grade.split()
    student_info = (student.name, student.surname, student.patronymic, student.group, grade[0],
                    grade[1], grade[2], grade[3])
    cursor.execute("INSERT INTO students (first_name, last_name, patronymic, \
    group_name, grade1, grade2, grade3, grade4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", student_info)
    con.commit()
    con.close()


def create_table():
    con = sqlite3.connect(BD_NAME)
    cursor = con.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    patronymic TEXT NOT NULL,
                    group_name TEXT NOT NULL,
                    grade1 INTEGER NOT NULL,
                    grade2 INTEGER NOT NULL,
                    grade3 INTEGER NOT NULL,
                    grade4 INTEGER NOT NULL
                )
            ''')
    con.commit()
    con.close()


def append_student():
    actions = ["Введите ФИО ученика, разделяя пробелами: ",
               "Введите его группу NNN(3 числа без пробелов): ",
               "Введите успеваемость(это 4 цифры разделенных пробелами; от 1 до 5): "]

    for i in range(3):
        while True:
            input_client = input(actions[i])
            if i == 0:
                if len(input_client.split()) == 3:
                    p = 0
                    for word in input_client.split():
                        if word.isalpha():
                            p += 1
                    if p == 3:
                        actions[0] = input_client.split()
                        break
            elif i == 1:
                if input_client.isdigit() and len(input_client) == 3:
                    actions[1] = input_client
                    break
            else:
                if len(input_client.split()) == 4:
                    p = 0
                    for char in input_client.split():
                        if char.isdigit() and len(char) == 1 and char in "12345":
                            p += 1
                    if p == 4:
                        actions[2] = input_client
                        break
            print("Указаны неверные данные!")
            print("Пробуй снова")

    new_student = Student(actions[0][0], actions[0][1], actions[0][2], actions[1], actions[2])
    add_student_bd(new_student)
    print(f"Добавлен сутдент: {actions[0][0]} {actions[0][1]} {actions[0][2]}; "
          f"В группе {actions[1]}; Успеваемость {actions[2]}")


def get_students():
    con = sqlite3.connect(BD_NAME)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    students_cursor = cursor.fetchall()
    con.close()
    all_students = []
    if students_cursor:
        for pers in students_cursor:
            all_students.append(Student(
                pers[1], pers[2], pers[3], pers[4], [pers[5], pers[6], pers[7], pers[8]],pers[0]
            ))
    else:
        return []
    return all_students


def get_student_average_grade(sid):
    if not sid.isdigit():
        print("Не верный ID")
        return

    con = sqlite3.connect(BD_NAME)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students WHERE id = (?)", (sid,))
    student_data = cursor.fetchone()
    con.close()
    if student_data:
        return Student(
            student_data[1],
            student_data[2],
            student_data[3],
            student_data[4],
            [student_data[5], student_data[6], student_data[7], student_data[8]],
            student_data[0]
        )
    else:
        return



def remake_student(sid):
    if not sid.isdigit():
        print("Не верный ID")
        return

    actions = ["Введите новое ФИО ученика, разделяя пробелами, если не надо, то #: ",
               "Введите его группу NNN(3 числа без пробелов), если не надо, то #: ",
               "Введите успеваемость(это 4 цифры разделенных пробелами; от 1 до 5), если не надо, то #: "]
    for i in range(3):
        while True:
            input_client = input(actions[i])
            if input_client == "#":
                break
            if i == 0:
                if len(input_client.split()) == 3:
                    p = 0
                    for word in input_client.split():
                        if word.isalpha():
                            p += 1
                    if p == 3:
                        remake_student_bd("name", input_client, sid)
                        break
            elif i == 1:
                if input_client.isdigit() and len(input_client) == 3:
                    remake_student_bd("group", input_client, sid)
                    break
            else:
                if len(input_client.split()) == 4:
                    p = 0
                    for char in input_client.split():
                        if char.isdigit() and len(char) == 1 and char in "12345":
                            p += 1
                    if p == 4:
                        actions[2] = input_client
                        remake_student_bd("grade", input_client, sid)
                        break
            print("Указаны неверные данные!")
            print("Пробуй снова")


def remove_student(sid):
    conn = sqlite3.connect(BD_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (sid,))
    conn.commit()
    rows_deleted = c.rowcount
    conn.close()

    if rows_deleted == 0:
        print("Никто не удален, ID не верен")
    else:
        print("Удален успешно!")
def awerage_grade_for_group(group):
    conn = sqlite3.connect(BD_NAME)
    c = conn.cursor()
    c.execute('''
            SELECT grade1, grade2, grade3, grade4 FROM students WHERE group_name = ?
        ''', (group,))
    rows = c.fetchall()
    conn.close()
    if not rows:
        print("Никого нет в группе")
        return
    total_sum = 0
    total_count = 0
    for grades in rows:
        total_sum += sum(grades)
        total_count += len(grades)
    print(f"В группе {group} средний балл: {total_sum / total_count}")


create_table()
while True:
    print("*" * 40)
    print("Это консольное приложение по работе со студентами")
    print("Что вы хотите сделать?")
    print("*" * 40)
    print("1. Добавить нового студента")
    print("2. Просмотр всех студентов")
    print("3. Просмотр студента и его ср.балл по ID")
    print("4. Редактирование студента")
    print("5. Удаление студента")
    print("6. Ср.балл у группы студентов")
    print("0. Иначе выход их программы")
    answer = input("\nДействие: ")
    if answer == "1":
        append_student()
    elif answer == "2":
        students = get_students()
        for stud in students:
            print(f"ID - {stud.id}; Студент: {stud.name} {stud.surname} {stud.patronymic}; Группа {stud.group}; "
                  f"Успеваемость ({stud.grade[0]} {stud.grade[1]} {stud.grade[2]} {stud.grade[3]})")
    elif answer == "3":
        id_sudent = input("Введите ID студента: ")
        student = get_student_average_grade(id_sudent)
        if student:
            stud_grade = [student.grade[0], student.grade[1], student.grade[2], student.grade[3]]
            print(f"ID - {student.id}; Студент: {student.name} {student.surname} {student.patronymic}; "
                  f"Средний балл: {sum(stud_grade) / len(stud_grade)}")
        else:
            print("Нет студента")
    elif answer == "4":
        id_sudent = input("Введите ID студента, которого надо редактировать: ")
        remake_student(id_sudent)
    elif answer == "5":
        id_sudent = input("Введите ID студента, которого надо удалить: ")
        remove_student(id_sudent)
    elif answer == "6":
        group_students = input("Введите номер группы: ")
        awerage_grade_for_group(group_students)
    else:
        print("Спасибо, что вы есть!")
        break
