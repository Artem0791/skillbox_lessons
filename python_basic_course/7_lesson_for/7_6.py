student_count = int(input('Сколько человек в классе? '))
grade_list = []
grade_3 = 0
grade_4 = 0
grade_5 = 0

for student in range(student_count):
    grade = int(input('Студент {} оценка: '.format(student+1)))
    if grade == 3:
        grade_3 += 1
    elif grade == 4:
        grade_4 += 1
    else:
        grade_5 += 1

if grade_3 > grade_4 and grade_3 > grade_5:
    print('сегодня больше троечников')
elif grade_4 > grade_3 and grade_4 > grade_5:
    print('сегодня больше хорошистов')
else:
    print('сегодня больше отличников')


    # еще один вариант решения
    # student_count = int(input('Сколько человек в классе? '))
    # grade_list = []
    # for student in range(student_count):
    #     grade = int(input('Студент {} оценка: '.format(student + 1)))
    #     grade_list.append(grade)
    #
    # grade_3 = grade_list.count(3)
    # grade_4 = grade_list.count(4)
    # grade_5 = grade_list.count(5)
    # if grade_3 > grade_4 and grade_3 > grade_5:
    #     print('сегодня больше троечников')
    # elif grade_4 > grade_3 and grade_4 > grade_5:
    #     print('сегодня больше хорошистов')
    # else:
    #     print('сегодня больше отличников')
    #


    # В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.
