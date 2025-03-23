"""
15. Создание класса:
Создайте класс Car с атрибутами brand, model и year.

Добавьте метод display_info(), который выводит информацию о машине.

Создайте объект этого класса и вызовите метод display_info().
"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Производитель: {self.brand}. Модель: {self.model}. Год выпуска: {self.year}")


car = Car('VAZ', '2111', '2003')
car.display_info()

"""
14. Работа с датами:
Используя модуль datetime, выведите текущую дату и время.

Добавьте к текущей дате 5 дней и выведите результат.
"""
# import datetime
# from datetime import timedelta
#
# print(datetime.date.today())
# today = datetime.date.today()
# today = today + timedelta(days=5)
# print(today)


"""
13. Исключения:
Напишите программу, которая запрашивает у пользователя число и выводит его квадрат.

Обработайте исключение, если пользователь вводит не число.

"""
# from sys import exception
#
# try:
#     n = int(input("Введите число для возведения в квадрат: "))
#     print("Квадрат числа равен: ", n**2)
# except Exception as e:
#     print("Error :", e)

"""12. Рекурсия:
Напишите рекурсивную функцию для вычисления факториала числа.
"""
# def Fac (x):
#     return x if x == 1 else Fac(x-1)*x
# print(Fac(10))

"""
Дополнительные задачи:
11. Сортировка:
Дан список строк: ["banana", "apple", "cherry", "date"].

Отсортируйте его в алфавитном порядке.

Отсортируйте его по длине строк.

"""
# fruit = ["banana", "apple", "cherry", "date"]
# print(fruit)
# fruit.sort()
# print(fruit)
# fruitsort=sorted(fruit, key=lambda x: len(x))
# print(fruitsort)


"""
10. Использование lambda и map():
Дан список чисел: [1, 2, 3, 4, 5].

Используя map() и lambda, создайте новый список, где каждое число умножено на 2.

Выведите результат.
"""
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)

"""
9. Работа с файлами:
Создайте текстовый файл example.txt и запишите в него несколько строк текста.

Напишите программу, которая читает этот файл и выводит количество строк в нём.
"""
# df = open("exemple.txt", "r", encoding="utf-8")
#
# for l1 in df:
#
#     print(l1)
# df.close()
"""
8. Генераторы списков:
Создайте список чисел от 1 до 10.

Используя генератор списков, создайте новый список, содержащий квадраты этих чисел.

Выведите результат.
"""
# num = [1, 2, 3, 4]
# num = [i for i in range(0, 100, 5) if i>0]
# squares = [i*i for i in num]
#
# print(num)
# print(squares)

"""
7. Словари:
Создайте словарь, где ключи — это имена людей, а значения — их возраст:

people = {"Alice": 25, "Bob": 30, "Charlie": 35}
Добавьте в словарь нового человека: "David": 40.

Измените возраст "Alice" на 26.

Удалите "Bob" из словаря.

Выведите итоговый словарь.

"""
#
# people = {'Alice': 25, 'Bob': 30, 'Charie': 35}
# print(people)
# people['David'] = 40
# print(people)
# people.pop('Bob')
# print(people)
#
# d1 = {"a": 1, "b": 2, "c": 3}
# print(d1)
# d1.update(people)
# print(d1)
# #Выводим ключи
# for key in d1:
#     print(key)
# #Выводим значения
# for value in d1.values():
#     print(value)
# #Выводим весь словарь
# for key, value in d1.items():
#     print(f"{key}: {value}")


"""
6. Работа с множествами:
Даны два множества:


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
Найдите пересечение этих множеств.

Найдите объединение этих множеств.

Найдите разность set1 и set2.
"""
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1)
# if set1 == set2:
#     print("equ")
# else:
#     print("not")
# print("пересечение ",set1 & set2)
# print('объединение ', set1|set2)
# print("разность ", set1^set2)#, set2-set1)
"""
5. Использование zip():

Даны два списка:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

Объедините их с помощью zip().
Преобразуйте результат в список кортежей.
Выведите имя и возраст каждого человека в формате: "Alice is 25 years old.".
# """
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# people = zip(names, ages)
# people_list = list(zip(*people))
#
# print(people_list)
# for name, age in zip(names, ages): #people_list:
#     print(f"{name} is {age} years old")
# i = 0
#
# while i <= len(people_list):
#     print(f"{people_list[0][i]} {people_list[1][i]} years old")
#     i+=1
# #
# # names = ["Alice", "Bob", "Charlie"]
# # ages = [25, 30, 35]
# #
# # for name, age in zip(names, ages):
# #     print(f"{name} is {age} years old.")
# #
"""
4. Операторы и условия:
Напишите программу, которая принимает от пользователя число и проверяет:

Если число положительное, выведите "Positive".

Если число отрицательное, выведите "Negative".

Если число равно нулю, выведите "Zero".

"""
# n=int(input("Введите число: "))
# if n == 0:
#     print('Zero')
# elif n < 0:
#     print("Negativ")
# else:
#     print("Positive")


"""
3. Функции:
Напишите функцию multiply(a, b), которая возвращает произведение двух чисел.

Напишите функцию is_even(n), которая возвращает True, если число чётное, и False — если нечётное.

Используйте эти функции в программе, чтобы проверить их работу.

"""
# def multiply(a, b):
#     return a * b
# print(multiply(2,2))
# def is_even(n):
#     return False if n % 2 else True
# n = input("Введите число для проверки его четности: ")
# print("Четное") if is_even(int(n)) else print('Нечетное')


"""
2. Работа со строками:
Дана строка: "Python is awesome!".

Преобразуйте строку в список слов.

Добавьте в конец списка слово "right?".

Объедините список обратно в строку с пробелами между словами.

Выведите результат.
"""
# string = 'Python is awesome!'
# str_as_list = string.split()
# print(str_as_list)
# str_as_list.append('right?')
# print(str_as_list)
# new_string = ' '.join(str_as_list)
# print(new_string)
#

"""
1. Работа со списками:
Создайте список из 10 чисел.

Добавьте в конец списка число 11.

Удалите второй элемент списка.

Найдите сумму всех элементов списка.

Выведите список в обратном порядке.
"""
# list = [1, 2, 3, 4, 5, 6, 7]
# list.append(11)
# list.pop(1)
# # sum=0
# # for elem in list:
# #     print(elem)
# #     sum+=int(elem)
# i=0
# sum=0
# while i < len(list):
#     # print(list[i])
#     sum+=list[i]
#     i+=1
#     print(list[len(list) - i])
#
# print(sum)
# list=list[::-1]
# list.reverse()
#
# print(list)
# #sum=summ(list)
