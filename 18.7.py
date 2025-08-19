# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Добавить ученика
        3. Удалить все данные по ученику
        4. Удалить предмет у всех учеников
        5. Удалить оценку ученика по предмету
        6. Редактировать данные по оценкам ученика
        7. Редактировать название предмета
        8. Редактировать данные по имени ученика
        9. Вывести средний балл по всем предметам по каждому ученику
        10. Вывести все оценки по всем ученикам
        11. Вывести все оценки определенного ученика
        12. Вывести средний балл по каждому предмету определенного ученика
        13. Вывести все оценки по определенному предмету
        14. Вывести лучших учеников по каждому предмету
        15. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in classes:
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Добавить ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # если данные введены верно
        if student not in students:
            # добавляем ученика
            students.append(student)
            print(f' {student} добавлен ')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: такой ученик уже существует')
        # создаем пустой словарь оценок, иначе дальнейшие запросы не будут работать
        students_marks[student] = {}
        # создаем пустой массив оценок по каждому предмету
        for class_ in classes:
            students_marks[student][class_] = []
            # запрашиваем оценки по каждому предмету
            marks = [int(value) for value in input(f'Введите оценки по предмету {class_} через пробел: ').split()]
            # проверяем правильность формата введенных оценок
            if all(0 < mark <= 5 for mark in marks):
                # записываем оценки по каждому предмету
                students_marks[student][class_] = marks
                print(f'Для ученика {student} добавлены оценки по предмету {class_} ')
            # неправильный формат оценок
            else:
                print(f'ОШИБКА: неверный формат оценок по предмету {class_} \n ВНИМИНИЕ: для дальнейшей корректной работы отредактируйте оценки с помощью команды 6 \n или удалите ученика {student} с помощью команды 3')
    elif command == 3:
        print('3. Удалить все данные по ученику')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # если данные введены верно
        if student in students:
            # удаляем все данные ученика
            students.remove(student)
            print(f'Для {student} все данные удалены ')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 4:
        print('4. Удалить предмет у всех учеников')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # если данные введены верно
        if class_ in classes:
            # удаляем предмет
            classes.remove(class_)
            print(f'Для предмета {class_} все данные удалены ')
        # неверно введено название предмета
        else:
            print('ОШИБКА: неверное название предмета')
    elif command == 5:
        print('5. Удалить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку, которую нужно удалить: '))
        # если данные введены верно
        if student in students and class_ in classes and mark in students_marks[student][class_]:
            # удаляем оценку для ученика по предмету
            students_marks[student][class_].remove(mark)
            print(f'Для ученика {student} по предмету {class_} удалена оценка {mark}')
        # неверно введены название предмета, имя ученика или оценка
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или оценка отсутствует')
    elif command == 6:
        print('6. Редактировать данные по оценкам ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценки, которые должны появиться после редактирования
        marks = [int(value) for value in input('Введите правильные оценки через пробел: ').split()]
        # если данные введены верно
        if all(0 < mark <= 5 for mark in marks) and student in students and class_ in classes:
            # очищаем список оценок для ученика по предмету
            students_marks[student][class_].clear()
            # записываем правильные оценки ученика по предмету
            students_marks[student][class_] = marks
            print(f'Для ученика {student} по предмету {class_} оценки скорректированы')
        # неверно введены название предмета, имя ученика или неправильный формат оценок
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или формат оценок')
    elif command == 7:
        print('7. Редактировать название предмета')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # если данные введены верно
        if class_ in classes:
            # считываем новое название предмета
            class_1 = input('Введите новое название предмета: ')
            # добавляем предмет с новым названием в список предметов
            classes.append(class_1)
            # создаем пустой массив оценок по новому предмету для всех учеников
            for student in students:
                # создаем пустой массив оценок по новому предмету
                students_marks[student][class_1] = []
                # запоминаем оценки ученика по предмету
                bufer = students_marks[student][class_]
                # очищаем список оценок по редактируемому предмету
                students_marks[student][class_] = []
                # записываем оценки в предмет с новым названием
                students_marks[student][class_1] = bufer
            classes.remove(class_)
            print(f'Название предмета {class_} изменено на {class_1} ')
        # неверно введено название предмета
        else:
            print('ОШИБКА: неверное название предмета')
    elif command == 8:
        print('8. Редактировать имя ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        student1 = input('Введите новое имя ученика: ')
        # если данные введены верно
        if student in students:
            # удаляем все данные ученика
            bufer = students_marks[student]
            # удаляем ученика из списка учеников
            students.remove(student)
            # добавляем новое имя ученика в сптсок учеников
            students.append(student1)
            # записываем оценки по предметам на новое имя ученика
            students_marks[student1] = bufer
            print(f'Имя ученика {student} изменено на {student1} ')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 9:
        print('9. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 10:
        print('10. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 11:
        print('11. Вывести все оценки определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students:
        # выводим словарь с оценками:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 12:
        print('12. Вывести средний балл по каждому предмету определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students:
        # выводим словарь с оценками:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'\t{class_} - {marks_sum // marks_count}')
            print()
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 13:
        print('13. Вывести все оценки по определенному предмету')
        # считываем имя ученика
        class_ = input('Введите название предмета: ')
        if class_ in classes:
            # выводим словарь с оценками:
            print(class_)
            # цикл по предметам
            for student in students:
                print(f'\t{student} - {students_marks[student][class_]}')
            print()
        # неверно введено название предмета
        else:
            print('ОШИБКА: неверное название предмета')
    elif command == 14:
        print('14. Вывести лучших учеников по каждому предмету')
        # цикл по предметам
        for class_ in classes:
            print(class_)
            # создаем пустой массив для определения наибольшей средней оценки по каждому предмету
            largest_mark = {}
            # цикл по ученикам
            for student in students:
                # создаем пустой массив для каждого ученика
                largest_mark[student] = {}
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # находим среднюю оценку
                mark_average = marks_sum // marks_count
                # определяем значения в массиве
                largest_mark[student] = mark_average
            # находим максимальный средний балл по каждому предмету
            max_value = max(largest_mark.values())
            # перебираем всех учеников и находим тех, средний балл которых равен максимальному
            for student in largest_mark.keys():
                if largest_mark[student] == max_value:
                    print(f'\t{student}')
        print()
    elif command == 15:
        print('15. Выход из программы')
        break
