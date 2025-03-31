
"""
🔹 Простые задачи на строки
1. Удвоение символов
Напиши функцию, которая принимает строку и возвращает новую строку, где каждый символ повторяется дважды.
Пример:
double_chars("abc") → "aabbcc"
double_chars("Привет") → "ППррииввеетт"
"""
# def double_chars(s):
#     return ''.join(list(ch * 2 for ch in s))
#
# print(double_chars("Хакас"))
"""
2. Удаление гласных
Напиши функцию, которая удаляет все гласные буквы (а, е, ё, и, о, у, ы, э, ю, я) из строки.
Пример:
remove_vowels("Программирование") → "Пргрммвн"  
"""
# def remove_vowels(s):
#     return ''.join(list(ch for ch in s if ch  not in 'аеёиоуыэюя'))
#
# print(remove_vowels("Программирование"))

"""
3. Замена цифр на слова
Напиши функцию, которая заменяет цифры в строке на их названия (0 → "ноль", 1 → "один" и т.д.).
Пример:
replace_numbers("Мне 5 лет") → "Мне пять лет"  
"""
# def replace_numbers(s):
#     L1 = s.split()
#     L2 = []
#     dict_int = {'1': 'один', '2': 'два', '3': 'три'}
#     # L = list(word for word in L if word not in "1234567890" else dict_int[word])
#     for word in L1:
#         if word in dict_int:
#             L2.append(dict_int[word])
#         else:
#             L2.append(word)
#     return ' '.join(L2)
#
# print(replace_numbers("Мне 2 года"))

"""
4. Первая и последняя буква
Напиши функцию, которая возвращает первую и последнюю букву строки. Если строка пустая, верни "".
Пример:
first_last("Python") → "Pn"  
first_last("А") → "АА"  
"""
# def first_last(s):
#     return s[0]+s[-1] if len(s) else ""
#
# print(first_last("sdfsd"))
"""    
5. Слова в обратном порядке
Напиши функцию, которая переворачивает порядок слов в строке (разделитель — пробел).
Пример:
reverse_words("Я учу Python") → "Python учу Я"  
"""
# def reverse_words(s):
#     return ' '.join(s.split()[::-1])
#
# print(reverse_words("sdffsdfdssdf"))
"""
🔹 Задача: "Шифр Цезаря" (простой сдвиг букв)
Напиши функцию caesar_cipher(text, shift), которая:

Принимает строку text и целое число shift (сдвиг).

Заменяет каждую букву в text на букву, стоящую в алфавите на shift позиций дальше.

Не изменяет символы, не являющиеся буквами (пробелы, цифры, знаки препинания).

Учитывает регистр (большие буквы остаются большими, маленькие — маленькими).

Примеры:

caesar_cipher("Hello, World!", 3)  → "Khoor, Zruog!"
caesar_cipher("АБВГД", 1)         → "БВГДЕ"
caesar_cipher("xyz", 2)           → "zab"  # (зацикливание алфавита)
💡 Подсказки:
Используй ord() (получить код символа) и chr() (преобразовать код в символ).

Для английских букв:

ord('A') = 65, ord('Z') = 90

ord('a') = 97, ord('z') = 122

Для русских букв:

ord('А') = 1040, ord('Я') = 1071

ord('а') = 1072, ord('я') = 1103

Не забудь про зацикливание (после 'я' идёт 'а').
"""

# def cipher(cod):
#     change = {91: 65, 92: 66, 123: 97, 124: 98, 1072: 1040, 1073: 1041, 1104: 1072, 1105: 1073}
#     if cod in change.key:
#         print(change.)

# def ceasar_cipher(word, d):
#     change = {91: 65, 92: 66, 123: 97, 124: 98, 1072: 1040, 1073: 1041, 1104: 1072, 1105: 1073}
#     ord_word = list(ord(ch) + 2 for ch in word)
#     cod_word = []
#     for ch in ord_word:
#         if int(ch) in change:
#             cod_word.append(chr(change[int(ch)]))
#         else:
#             cod_word.append(chr(ch))
#     return ''.join(cod_word)
#
#
# #
# print(ceasar_cipher("xyz", 2))

"""
Izuchaem Python. Lutz
"""

"""
🔹 Задания на строки (с решениями в конце)
1. Обращение строки
Напиши функцию, которая принимает строку и возвращает её в обратном порядке.
Пример:
reverse_string("Привет") → "тевирП"
"""

# def reverse_string(s):
#     if type(s) == str:
#         s = s[::-1]
#         print(s)
#     else:
#         print("It`s not str")
#     return s
#
#
# reverse_string("Привет")

# def count_vowels(s):
#     vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
#     print(list(char in s for char in vowels))
#     return sum(1 for char in s if char in vowels)
#
# print(count_vowels("Программирование"))  # 6

"""
2. Подсчёт гласных
Напиши функцию, которая считает количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в строке.
Пример:
count_vowels("Программирование") → 6
"""

# def count_vowels(s):
#     vowels = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
#     n = 0
#     if type(s) == str:
#         for c in s:
#             print(c)
#             if c in vowels:
#                 print("+++")
#                 n += 1
#         print(n)
#     else:
#         print("It`s not str type")
#     return n
#
# def count_vowels2(s):
#     vowels = ('аеёиоуыэюя')
#     n = 0
#     for ch in s:
#         n += vowels.count(ch)
#     print(n)
#     return n

# s = "Программииииирование"
# count_vowels(s)
# count_vowels2(s)

"""
3. Проверка на палиндром
Напиши функцию, которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево, без учёта регистра и пробелов).
Пример:
is_palindrome("А роза упала на лапу Азора") → True
"""
# def is_palidrome(s):
#     s = s.replace(" ","")
#     s = s.lower()
#     h = len(s) // 2
#     # l = len(s)
#     # if l % 2 == 0:
#     #     begin_s= s[:h]
#     #     end_s = s[h:]
#     #     print(begin_s, " ", end_s)
#     # else:
#     #     begin_s= s[:h]
#     #     end_s = s[h+1:]
#     #     print("Число букв нечетное ", begin_s, " ", end_s)
#     # print(s)
#     pali = True
#     for i in range(h):
#         pali = True * s[i] == s[-i-1]
#         # print(s[i], " == ", s[-i-1], "it`s ", pali)
#     print("Result", pali)
#     return pali
#
# is_palidrome("А роза упала нна лапу Азора")

"""
4. Замена символов
Напиши функцию, которая заменяет все пробелы в строке на _ (нижнее подчёркивание).
Пример:
replace_spaces("Это тестовая строка") → "Это_тестовая_строка"
"""
# def replace_spaces(s):
#     s = s.replace(" ","_")
#     return s
#
# s = "Это тестовая строка"
# s = replace_spaces(s)
# print(s)
"""
# 5. Форматирование имени
# Напиши функцию, которая принимает имя и фамилию, а возвращает строку в формате "Фамилия, И." (первая буква имени + точка).
# Пример:
# format_name("Иван", "Петров") → "Петров, И."
"""
# def format_name(fname, sname):
#     return fname + ", " + sname[0] + "."
#
# print(format_name("Karchenko", "Andrey"))
"""
📌 Задание: Калькулятор расходов
Цель:
Написать программу, которая записывает и анализирует ежедневные траты пользователя.

🔹 Что нужно сделать:
Ввод данных:

Пользователь вводит сумму расхода и категорию (например: "Еда", "Транспорт", "Развлечения").

Данные сохраняются в словаре или списке.

Анализ расходов:

Программа выводит общую сумму трат.

Показывает, сколько потрачено по каждой категории.

Дополнительно (по желанию):

Сохранение данных в файл (чтобы они не пропадали после закрытия программы).

Возможность просмотра всех трат за выбранный день.
"""  #
# from dateutil.parser import parse
#
#
# # Функция возвращает дату введенную пользователем типа class 'datetime.date'>
# # Надо придумать как записывать ее в строку или записывать и читать из файла в таком виде
# def input_date():
#     date_str = input('Введите дату: ')
#     try:
#         user_date = parse(date_str).date
#         print('Распознана дата: ', user_date())
#     except ValueError as val_er:
#         print('Не удалось распознать дату: ', val_er)
#     return user_date()
#
#
# # Функции по работе со строками для закрепления знаний полученных из книги Лутца
# def teach_str():
#     # Практикуем срезы
#     # N = 'Andrey'
#     # F = 'Karchenko'
#     # L = N[0:-1] + F[1:]
#     # Практикуем форматированный вывод
#     L = 'Выводим числа: {2:X}, {1:-120,.5}, {0:.3}'.format(2.1231243124, 3 / 7, 255)
#
#     return L


# Проверка написанных функций

# Проверка функции получения даты от пользователя
# date = input_date()
# print(type(date), '{}'.format(date))
#
# L = teach_str()
# print(L)
#
# #
# from pathlib import Path

#
# data = {}
# #
# lines = Path("expenses.txt").read_text(encoding="utf-8")  # .splitlines()
# # print(lines)
# s_expended = lines.split("\n")
# i = 0
# for n in s_expended:
#     data[i] = n.split(', ')
#     #    print(data[i])
#     i += 1
# data[6] = ['2012.12.12', 'cookis', '1000']
# print(data[0][2])
# print(len(data[1][1]))
# data[6] = ['2012.12.12', 'cookis', '1000']
# suma = 0
# for exp in data:
#     #   print(data[exp][2])
#     suma += int(data[exp][2])
# print(suma)
#
# "Output row matrix"
# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# col2 = [row2[1] for row2 in M]
# print(col2)
#
# col2 = [row[1] + 1 for row in M]  # Добавить 1 к каждому элементу в столбце 2
# print(col2)
# col2 = [row[1] for row in M if row[1] % 2 == 0]  # Отфильтровать нечетные элементы
# print(col2)
#
# diag = [M[i][i] for i in [0, 1, 2]]  # Собрать диагональ из матрицы
# print(diag)
# # [1, 5, 9]
#
# doubles = [c * 2 for c in 'spam']  # Повторить символы в строке
# print(doubles)
#
# L = list(range(4))
# print(L)
# L = list(range(-6, 7, 2))  # от -6 до +6 с шагом 2
# # [-6, -4, -2, 0, 2, 4, 6]
# # 0. . 3 (в Python З.Х требуется вызов list ())
# # (в Python З.Х нужен вызов list())
# print(L)
#
# L = [[x ** 2, x ** 3] for x in range(4)]  # Множество значений, фильтры if
# # [[О, 0], [1, 1], [4, 8], [9, 27]]
# L = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
# # [[2, 1, 4], [4, 2, 8], [6, 3, 12]]
# print(L)

# print('s_expended[0] ', s_expended[1])
# print(len(s_expended))
# for line in Path("expenses.txt").read_text(encoding="utf-8").splitlines():
#     if ":" in line:
#         key, value = line.split(":", maxsplit=1)
#         data[key.strip()] = value.strip()


# from pathlib import Path
# 1=0
# lines = Path("expenses.txt").read_text(encoding="utf-8").splitlines()
# for line in lines:
#     L=
#     print(line)

# content=Path("expenses.txt").read_text(encoding="utf-8")
# print(content)
#
# l=content
# # expenses = {}
# lines = []
# with open("expenses.txt", "r", encoding="utf-8") as file:
#     n = file.readline()
#         for line in file:
#             lines=
#
# with open("file.txt", "r", encoding="utf-8") as file:
#     line = file.readline()  # Читает одну строку
#     while line:
#         print(line.strip())  # Удаляем лишние пробелы и переносы
#         line = file.readline()

# from pathlib import Path
#
# content = Path("expenses.txt").read_text(encoding="utf-8")
# print(content)
