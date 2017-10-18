#!/usr/bin/env python3

while True:
    try:
        h = float(input('Введите рост в сантиметрах: '))/100
        m = float(input('Введите массу в килограммах: '))

        if h < 0 or m < 0:
            raise ValueError
        i = m / h ** 2

        break
    except (ValueError, ZeroDivisionError):
        print('Что-то не так с Вашим ростом и весом...')



results_table = (
    (16, 'Выраженный дефицит массы тела'),
    (18.5, 'Недостаточная (дефицит) масса тела'),
    (24.99, 'Норма'),
    (25, 'Дыра в таблице Википедии (https://ru.wikipedia.org/wiki/Индекс_массы_тела)'),
    (30, 'Избыточная масса тела (предожирение)'),
    (35, 'Ожирение первой степени'),
    (40, 'Ожирение второй степени'),
    (float('infinity'), 'Ожирение третьей степени (морбидное)'),)

for result, message in results_table:
    if i < result:
        print(message)
        break
