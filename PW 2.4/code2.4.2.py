"""Разработайте приложение „I love drink“, со следующим
функционалом:
1) Учет напитков:
1.1) Хранение данных об алкогольных напитках и ингредиентах
1.2) Учет остатков на складе
2) Управление коктейлями:
2.1) Хранение данных о коктейлях(название,
крепость(автоматический расчет исходя из крепости алкогольных
напитков), состав, цена)
3) Операции
3.1) Продажа коктейлей и алкогольных напитков
3.2) Пополнение запасов
В приложении должна использоваться база данных для хранения
информации. """

import sqlite3

BD_NAME = "drink_store.bd"


class DataBase:

    def __new__(cls, *args, **kwargs):
        raise TypeError("Этот класс нельзя инстанцировать")

    @staticmethod
    def create_table(table_prompt):
        con = sqlite3.connect(BD_NAME)
        cursor = con.cursor()
        cursor.execute(table_prompt)
        con.commit()
        con.close()

    @staticmethod
    def add_info_in_table(table_name, **dict_info):

        columns = ', '.join(dict_info.keys())
        placeholders = ', '.join(['?'] * len(dict_info))
        values = list(dict_info.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        con = sqlite3.connect(BD_NAME)
        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        con.close()

    @staticmethod
    def add_info_in_table_and_return_id(table_name, **dict_info):

        columns = ', '.join(dict_info.keys())
        placeholders = ', '.join(['?'] * len(dict_info))
        values = list(dict_info.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        con = sqlite3.connect(BD_NAME)
        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        answer_id = cursor.lastrowid
        con.close()
        return answer_id

    @staticmethod
    def delete_info_in_table(table_name, column_name, sid):
        con = sqlite3.connect(BD_NAME)
        cursor = con.cursor()
        s = f"DELETE FROM {table_name} WHERE {column_name} = ?"
        cursor.execute(s, (sid,))
        con.commit()
        if cursor.rowcount > 0:
            print(f"Продукт с ID {sid} успешно удален.")
        else:
            print(f"Продукт с ID {sid} не найден.")
        con.close()

    @staticmethod
    def get_info_in_table(table_name):
        con = sqlite3.connect(BD_NAME)
        cursor = con.cursor()

        cursor.execute(f"SELECT name FROM sqlite_master WhERE type='table' AND name='{table_name}';")

        cursor.execute(f"SELECT * FROM {table_name}")
        info_something = cursor.fetchall()
        con.close()
        if info_something:
            return info_something
        else:
            print("Нет записей в таблице!")





class The_Best_Application_Of_Drinks(DataBase):
    @staticmethod
    def play():
        DataBase.create_table("""
        CREATE TABLE IF NOT EXISTS cocktail (
            id_cocktail INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            strength REAL NOT NULL
        );
    """)
        DataBase.create_table("""
                CREATE TABLE IF NOT EXISTS cocktail_ingredients (
                    id_cocktail INTEGER,
                    ingredient TEXT NOT NULL,
                    FOREIGN KEY (id_cocktail) REFERENCES cocktail (id_cocktail)
                );
            """)
        DataBase.create_table("""
                        CREATE TABLE IF NOT EXISTS cocktail_drinks (
                            id_cocktail INTEGER,
                            drink TEXT NOT NULL,
                            volume REAL NOT NULL,
                            strength REAL NOT NULL,
                            FOREIGN KEY (id_cocktail) REFERENCES cocktail (id_cocktail)
                        );
                    """)

        DataBase.create_table(""" 
        CREATE TABLE IF NOT EXISTS drinks (
            id_drinks INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            volume REAL NOT NULL,
            strength REAL NOT NULL,
            price REAL NOT NULL
        );
    """)
        DataBase.create_table("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id_ingredients INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
    """)

        while True:
            print("*" * 40)
            print("КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ ПО ВЫПИВКЕ")
            print("*" * 40)
            print("Что будем делать?")
            print("1. Посмотреть ресурсы на складе")
            print("2. Добавить на склад")
            print("3. Продать товар")
            answer1 = input("Выбор: ")
            if answer1 == "1":
                print("1. Смотреть ингридиенты")
                print("2. Смотреть напитки")
                print("3. Смотреть коктели")
                answer2 = input("Выбор: ")
                if answer2 == "1":
                    info = DataBase.get_info_in_table("ingredients")
                    if info is not None:
                        for i in info:
                            print(f"ID: {i[0]}; Название: {i[1]}; Цена: {i[2]}")
                elif answer2 == "2":
                    info = DataBase.get_info_in_table("drinks")
                    if info is not None:
                        for i in info:
                            print(f"ID: {i[0]}; Название: {i[1]}; Объем: {i[2]}; Крепкость: {i[3]}; Цена: {i[4]}")
                elif answer2 == "3":
                    info1 = DataBase.get_info_in_table("cocktail")
                    if info1 is not None:
                        for i in info1:
                            print(f"ID: {i[0]}; Название: {i[1]}; Цена: {i[2]}; Крепкость: {i[3]:.2f}")
                    print("Напипши ID коктеля и cocktail_ingredients/cocktail_drinks")
                    print("через 1 пробел, чтобы увидеть подрбную информацию об ингридиентах/напитках в коктеле")
                    print("Например: 1 cocktail_ingredients")
                    print("Иначе ничего")
                    answer3 = input("Выбор: ").split()
                    arr_ans = ("cocktail_ingredients", "cocktail_drinks")
                    if len(answer3) == 2 and answer3[0].isdigit() and answer3[1] in arr_ans:
                        info2 = DataBase.get_info_in_table(answer3[1])
                        if info2 is not None:
                            if answer3[1] == arr_ans[0]:
                                for i in info2:
                                    if answer3[0] == str(i[0]):
                                        print(f"ID: {i[0]}; Название: {i[1]}")
                            elif answer3[1] == arr_ans[1]:
                                for i in info2:
                                    if answer3[0] == str(i[0]):
                                        print(f"ID: {i[0]}; Название: {i[1]}; Объем: {i[2]}; Крепкость: {i[3]}")

                    else:
                        continue
                else:
                    continue

            elif answer1 == "2":
                print("1. Добавить ингридиент")
                print("2. Добавить напиток")
                print("3. Добавить коктель")
                answer2 = input("Выбор: ")
                if answer2 == "1":
                    inp1 = input("Введите название для ингридиента: ")
                    inp2 = int(input("Введите цену для ингридиента: "))
                    DataBase.add_info_in_table("ingredients", name=inp1, price=inp2)
                elif answer2 == "2":
                    inp1 = input("Введите название для напитка: ")
                    inp2 = float(input("Введите объем для напитка: "))
                    inp3 = float(input("Введите крепкость для напитка(Например: 13.333): "))
                    inp4 = float(input("Введите цену для напитка: "))
                    DataBase.add_info_in_table("drinks",
                                               name=inp1, volume=inp2, strength=inp3, price=inp4)
                elif answer2 == "3":
                    inp1 = input("Введите название для коктеля: ")
                    inp2 = float(input("Введите цену для коктеля: "))
                    print("Коктель должен состоять из напитков, укажите как в примере, рядом укзывать объем в мл и "
                          "крепкость в процентах")
                    print("Пример: СокЯблочный,200,0 Водка,100,20 Гринтвейн,50,50")
                    inp3 = input("Ввод: ")

                    if not inp3.split():
                        print("Коктель не был создан, укажите напитки!")
                        continue
                    inp4 = input("В коктеле могут быть ингридиенты, укажите их чрезз пробел: ")

                    correct_cocktail_info = [(i.split(",")) for i in inp3.split()]
                    total_volume = 0
                    total_strength = 0
                    for drink in [i[1:3] for i in correct_cocktail_info]:
                        total_volume += float(drink[0])
                        total_strength += float(drink[1]) * float(drink[0])
                    cocktail_strength = total_strength / total_volume



                    primary_key = DataBase.add_info_in_table_and_return_id("cocktail",
                                                                           name=inp1, price=inp2,
                                                                           strength=cocktail_strength)
                    for drink in correct_cocktail_info:
                        DataBase.add_info_in_table("cocktail_drinks",
                                                   drink=drink[0], volume=drink[1], strength=drink[2],
                                                   id_cocktail=primary_key)
                    for ingredient in inp4.split():
                        DataBase.add_info_in_table("cocktail_ingredients",
                                                   ingredient=ingredient, id_cocktail=primary_key)

                else:
                    continue

            elif answer1 == "3":
                print("1. Продать ингридиент")
                print("2. Продать напиток")
                print("3. Продать коктель")
                answer2 = input("Выбор: ")
                if answer2 == "1":
                    answer3 = input("Введите ID продаваемого ингридиента: ")
                    DataBase.delete_info_in_table("ingredients", "id_ingredients",  answer3)
                elif answer2 == "2":
                    answer3 = input("Введите ID продаваемого напитка: ")
                    DataBase.delete_info_in_table("drinks","id_drinks", answer3)
                elif answer2 == "3":
                    answer3 = input("Введите ID продаваемого коктеля: ")
                    DataBase.delete_info_in_table("cocktail", "id_cocktail", answer3)
                    DataBase.delete_info_in_table("cocktail_ingredients", "id_cocktail", answer3)
                    DataBase.delete_info_in_table("cocktail_drinks", "id_cocktail", answer3)
                else:
                    continue
            else:
                break


The_Best_Application_Of_Drinks.play()
